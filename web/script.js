document.addEventListener("DOMContentLoaded", () => {

    // Page entrance
    document.body.classList.add("page-loaded");

    // Elements
    const sections = document.querySelectorAll("main section");
    const navLinks = document.querySelectorAll(".nav-links a");
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector(".nav-links");

    // Mobile menu
    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", () => {
            navMenu.classList.toggle("open");
        });
    }

    // Scroll reveal + active navigation
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("visible");

                    navLinks.forEach((link) => {
                        link.classList.remove("active");

                        if (
                            link.getAttribute("href") ===
                            `#${entry.target.id}`
                        ) {
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

                // Close mobile menu
                if (navMenu) {
                    navMenu.classList.remove("open");
                }
            }
        });
    });

});
// ---------- PROJECT DATA ----------

const projects = [
    {
        id: 1,
        name: "AI-Portfolio",
        description:
            "A personal portfolio system built while learning Python, Git, GitHub, HTML, and CSS.",
        status: "IN DEVELOPMENT",
        technologies: [
            "Python",
            "Git",
            "GitHub",
            "HTML",
            "CSS"
        ],
        github: "https://github.com/tharun-8t/AI-Portfolio"
    },
        {
        id: 2,
        name: "Student Expense Tracker",
        description:
            "A simple project for recording and organizing daily student expenses.",
        status: "PLANNED",
        technologies: [
            "Python",
            "Data Handling",
            "Git"
        ],
        github: "https://github.com/tharun-8t/AI-Portfolio"
    }
];

const projectsContainer = document.querySelector("#projects-container");

if (projectsContainer) {
    projects.forEach((project) => {

        const card = document.createElement("article");
        card.className = "project-card";

        card.innerHTML = `
            <div class="project-top">
                <span class="project-number">
                    ${String(project.id).padStart(2, "0")}
                </span>

                <span class="project-status">
                    ${project.status}
                </span>
            </div>

            <h3>${project.name}</h3>

            <p>
                ${project.description}
            </p>

            <div class="project-tech">
                ${project.technologies
                    .map((technology) => `<span>${technology}</span>`)
                    .join("")}
            </div>

            <a
                href="${project.github}"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link">
                View on GitHub →
            </a>
        `;

        projectsContainer.appendChild(card);
    });
}