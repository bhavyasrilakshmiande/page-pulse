document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("auditButton");
  const urlInput = document.getElementById("urlInput");
  const loading = document.getElementById("loading");
  const result = document.getElementById("result");
  const error = document.getElementById("error");

  let lastResponse = null;

  button.addEventListener("click", async () => {
    const url = urlInput.value.trim();

    if (!url) {
      alert("Please enter a URL");
      return;
    }

    loading.classList.remove("hidden");
    result.classList.add("hidden");
    error.classList.add("hidden");

    try {
      const response = await fetch("/audit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      loading.classList.add("hidden");

      if (!data.success) {
        error.classList.remove("hidden");
        document.getElementById("errorMessage").textContent = data.error;
        return;
      }

      lastResponse = data;

      result.classList.remove("hidden");

      document.getElementById("httpStatus").textContent = data.http_status;
      document.getElementById("responseTime").textContent =
        data.response_time.toFixed(2);
      document.getElementById("pageTitle").textContent = data.page_title;
      document.getElementById("metaDescription").textContent =
        data.meta_description || "Not Available";
      document.getElementById("h1Count").textContent = data.h1_count;
      document.getElementById("imagesMissingAlt").textContent =
        data.images_missing_alt;
      document.getElementById("wordCount").textContent = data.word_count;
    } catch (err) {
      loading.classList.add("hidden");
      error.classList.remove("hidden");
      document.getElementById("errorMessage").textContent = err.message;
    }
  });

  document.getElementById("copyJsonButton").addEventListener("click", () => {
    if (lastResponse) {
      navigator.clipboard.writeText(JSON.stringify(lastResponse, null, 2));
      alert("JSON copied!");
    }
  });

  document
    .getElementById("clearResultsButton")
    .addEventListener("click", () => {
      urlInput.value = "";

      result.classList.add("hidden");
      error.classList.add("hidden");
      loading.classList.add("hidden");

      document.getElementById("httpStatus").textContent = "";
      document.getElementById("responseTime").textContent = "";
      document.getElementById("pageTitle").textContent = "";
      document.getElementById("metaDescription").textContent = "";
      document.getElementById("h1Count").textContent = "";
      document.getElementById("imagesMissingAlt").textContent = "";
      document.getElementById("wordCount").textContent = "";

      lastResponse = null;
    });
});
