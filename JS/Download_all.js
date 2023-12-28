document.addEventListener("DOMContentLoaded", function () {
    const downloadAllButton = document.getElementById("download-all");
  
    downloadAllButton.addEventListener("click", async function () {
      try {
        const response = await fetch("http://${process.env.HOST_PC}:${process.env.PORT}/download-all");
  
        if (response.ok) {
          // Trigger the download of all files
          const blob = await response.blob();
          const link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);
          link.download = "all_files.zip";
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        } else {
          console.error("Error downloading all files:", response.statusText);
        }
      } catch (error) {
        console.error("Error downloading all files:", error);
      }
    });
  });
  