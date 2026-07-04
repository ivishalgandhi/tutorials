package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
)

func main() {
	secret := "test-secret"

	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		body, _ := io.ReadAll(io.LimitReader(r.Body, 1<<20))
		r.Body.Close()

		got := r.Header.Get("X-Signature")
		want := hex.EncodeToString(hmacHash(body, secret))

		// BUG: comparing signatures with == is vulnerable to timing attacks.
		if got != want {
			http.Error(w, "invalid signature", http.StatusUnauthorized)
			return
		}
		fmt.Fprint(w, "ok")
	})

	payload := []byte(`{"event":"push"}`)
	req := httptest.NewRequest(http.MethodPost, "/", strings.NewReader(string(payload)))
	req.Header.Set("X-Signature", hex.EncodeToString(hmacHash(payload, secret)))

	rec := httptest.NewRecorder()
	handler.ServeHTTP(rec, req)
	fmt.Println(rec.Code, rec.Body.String())
}

func hmacHash(data []byte, secret string) []byte {
	h := hmac.New(sha256.New, []byte(secret))
	h.Write(data)
	return h.Sum(nil)
}
