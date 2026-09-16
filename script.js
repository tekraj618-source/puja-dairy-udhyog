const form = document.getElementById("inquiryForm");
const statusText = document.getElementById("formStatus");

function openInquiry(productName) {
    document.getElementById("product").value = productName;
    document.getElementById("contact").scrollIntoView({ behavior: "smooth" });
    setTimeout(() => document.getElementById("name").focus(), 600);
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    statusText.textContent = "Sending...";
    statusText.style.color = "#176b2b";

    const payload = {
        name: document.getElementById("name").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        product: document.getElementById("product").value,
        message: document.getElementById("message").value.trim()
    };

    try {
        const response = await fetch("/api/contact", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) throw new Error(data.message);

        statusText.textContent = data.message;
        form.reset();
    } catch (error) {
        statusText.textContent = error.message || "Something went wrong. Please try again.";
        statusText.style.color = "#a33";
    }
});
