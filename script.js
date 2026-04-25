// -----------------------------
// UNIVERSAL AUTH CHECK (only runs on pages that require it)
// -----------------------------
function requireAuth() {
    const token = localStorage.getItem("token");
    if (!token) {
        window.location.href = "/login";
    }
}

async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const res = await fetch("http://localhost:8000/auth/login", {
    method: "POST",
    headers:{},
    body: new URLSearchParams({
        username: username,
        password: password
    })
});

    if (!res.ok) {
        alert("Invalid username or password");
        return;
    }

    const data = await res.json();
    localStorage.setItem("token", data.access_token);

    window.location.href = "/app";
}




// -----------------------------
// SIGNUP FUNCTION
// -----------------------------
async function signup() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch("http://localhost:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    if (!res.ok) {
        alert("Signup failed — username may already exist");
        return;
    }

    alert("Account created! Please log in.");
    window.location.href = "/login";
}

// -----------------------------
// LOGOUT FUNCTION
// -----------------------------
function logout() {
    localStorage.removeItem("token");
    window.location.href = "/login";
}

// -----------------------------
// UNIVERSAL AUTH FETCH WRAPPER
// -----------------------------
async function authFetch(url, options = {}) {
    const token = localStorage.getItem("token");

    if (!token) {
        window.location.href = "/login";
        return;
    }

    options.headers = options.headers || {};
    options.headers["Authorization"] = "Bearer " + token;

    return fetch(url, options);
}

// -----------------------------
// LOAD PLAYERS
// -----------------------------
async function loadPlayers() {
    requireAuth();

    const res = await authFetch("http://localhost:8000/players");

    if (!res.ok) {
        alert("Session expired. Please log in again.");
        logout();
        return;
    }

    const data = await res.json();
    console.log("Players:", data);

    // TODO: render players to the page
}

// -----------------------------
// ADD PLAYER
// -----------------------------
async function addPlayer() {
    requireAuth();

    const name = document.getElementById("name").value;
    const points = Number(document.getElementById("points").value);

    const res = await authFetch("http://localhost:8000/players", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, points })
    });

    if (!res.ok) {
        alert("Failed to add player");
        return;
    }

    const data = await res.json();
    console.log("Player added:", data);

    loadPlayers();
}
// Delete player
            async function deletePlayer(id) {
            await fetch(`${API_URL}/players/${id}`, {
            method: "DELETE",
            headers: { Authorization: `Bearer ${token}` },
            });
        loadPlayers();
        }