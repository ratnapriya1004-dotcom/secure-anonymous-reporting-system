const form = document.getElementById("reportForm");
const msg = document.getElementById("successMsg");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    // Simulating report submission (backend will be added later)
    msg.classList.remove("hidden");

    // Clear form
    form.reset();
});
