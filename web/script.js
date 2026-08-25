// Page entrance

document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("page-loaded");

    const sections = document.querySelectorAll("main section");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        },
        {
            threshold: 0.15
        }
    );

    sections.forEach((section) => {
        section.classList.add("reveal");
        observer.observe(section);
    });
});