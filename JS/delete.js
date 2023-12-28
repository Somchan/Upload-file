function deleteFile(filename) {
    if (confirm(`Are you sure you want to delete ${filename}?`)) {
      fetch(`http://${process.env.HOST_PC}:${process.env.PORT}/delete/${filename}`, {
        method: 'DELETE',
      })
        .then(response => {
          if (response.ok) {
            console.log(`File ${filename} deleted successfully.`);
            const listItem = document.querySelector(`li[data-filename="${filename}"]`);
            if (listItem) {
              listItem.remove();
            }
          } else {
            console.error(`Error deleting file ${filename}: ${response.statusText}`);
          }
        })
        .catch(error => {
          console.error(`Error deleting file ${filename}: ${error}`);
        });
        window.location.reload();
    }
  }
