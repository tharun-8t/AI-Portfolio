// Page entrance + scroll reveal

document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("page-loaded");

    const sections = document.querySelectorAll("main section");
    const navLinks = document.querySelectorAll(".nav-links a");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");

                    navLinks.forEach((link) => {
                        link.classList.remove("active");

                        if (link.getAttribute("href") === `#${entry.target.id}`) {
                            link.classList.add("active");
                        }
                    });
                }
            });
        },
        {
            threshold: 0.15,
                rootMargin: "-10% 0px -60% 0px"
        }
    );

    sections.forEach((section) => {
        section.classList.add("reveal");
        observer.observe(section);
    });

    // Smooth navigation
    navLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();

            const targetId = link.getAttribute("href");
            const target = document.querySelector(targetId);

            if (target) {
                target.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });
});