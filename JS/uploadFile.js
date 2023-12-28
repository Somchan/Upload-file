function updateFileNames() {
    const fileInput = document.getElementById("fileInput");
    const fileNameLabel = document.getElementById("fileNameLabel");
  
    if (fileInput.files.length > 0) {
      const fileNames = Array.from(fileInput.files).map((file) => file.name);
      fileNameLabel.innerText = fileNames.join(", ");
    } else {
      fileNameLabel.innerText = "Choose files";
    }
  }
  
  async function uploadFiles() {
    const fileInput = document.getElementById("fileInput");
    const files = fileInput.files;
  
    if (!files || files.length === 0) {
      console.error("No files selected for upload.");
      return;
    }
  
    try {
      const formData = new FormData();
      for (const file of files) {
        formData.append("files", file);
      }
  
      const progressBar = document.getElementById("progress-bar");
      const progressBarInner = document.getElementById("progress-bar-inner");
  
      progressBar.style.display = "block";
  
      const xhr = new XMLHttpRequest();
  
      // Set up the event listener for progress
      xhr.upload.addEventListener("progress", function (event) {
        if (event.lengthComputable) {
          const percentComplete = (event.loaded / event.total) * 100;
          progressBarInner.style.width = percentComplete + "%";
          progressBarInner.innerHTML = Math.round(percentComplete) + "%";
        }
      });
  
      xhr.open("POST", "http://${process.env.HOST_PC}:${process.env.PORT}/upload/");
      xhr.send(formData);
  
      const response = await new Promise((resolve, reject) => {
        xhr.onreadystatechange = function () {
          if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              resolve(JSON.parse(xhr.responseText));
            } else {
              reject(new Error("Failed to upload files"));
            }
          }
        };
      });
  
      console.log("API Response:", response);
  
      // Refresh the page after a successful upload
      window.location.reload();
    } catch (error) {
      console.error("API Request Error:", error);
    }
  }
  