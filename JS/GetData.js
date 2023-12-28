document.addEventListener("DOMContentLoaded", async function () {
    // Fetch data from http://localhost:8000/get
    try {
      const response = await fetch("http://${process.env.HOST_PC}:${process.env.PORT}/get");
      const data = await response.json();
  
      // Get the file list element
      const fileList = document.getElementById("file-list");
  
      // Clear existing content
      fileList.innerHTML = "";
  
      // Iterate over files and add them to the list
      data.files.forEach((file) => {
        const listItem = document.createElement("li");
        listItem.className = "list-group-item";
  
        const innerDiv = document.createElement("div");
        innerDiv.className = "d-flex justify-content-between align-items-center";
  
        const label = document.createElement("label");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = "selected_files";
        checkbox.value = file;
        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(` ${file}`));
  
        const btnGroup = document.createElement("div");
        btnGroup.className = "btn-group";
  
        const downloadBtn = document.createElement("a");
        downloadBtn.href = `/download/${file}`;
        downloadBtn.className = "btn btn-primary btn-sm";
        downloadBtn.innerText = "Download";
        downloadBtn.setAttribute("download", "");
  
        const deleteBtn = document.createElement("button");
        deleteBtn.className = "btn btn-danger btn-sm delete-button";
        deleteBtn.setAttribute("data-filename", file);
        deleteBtn.innerText = "Delete";
        deleteBtn.onclick = function () {
          deleteFile(file);
        };
  
        btnGroup.appendChild(downloadBtn);
        btnGroup.appendChild(deleteBtn);
  
        innerDiv.appendChild(label);
        innerDiv.appendChild(btnGroup);
  
        listItem.appendChild(innerDiv);
        fileList.appendChild(listItem);
        
        
      });
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  });