const res = await fetch("https://fa9cr1f2g3.execute-api.eu-north-1.amazonaws.com/develop/users/login", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ username: "admin", password: "password" })
});
console.log("Status:", res.status);
const text = await res.text();
console.log("Respuesta:", text);