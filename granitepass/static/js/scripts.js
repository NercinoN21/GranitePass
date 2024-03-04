document.addEventListener("DOMContentLoaded", function() {
    console.log("O documento HTML foi carregado!");

    const header = document.querySelector("h1");
    header.addEventListener("mouseenter", function() {
        this.style.backgroundColor = "#555";
    });
    header.addEventListener("mouseleave", function() {
        this.style.backgroundColor = "#fff";
    });
});