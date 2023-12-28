async function downloadFile(filename) {
  try {
    const response = await fetch(`http://${process.env.HOST_PC}:${process.env.PORT}/download/${filename}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/octet-stream',
      },
    });

    if (response.ok) {
      const blob = await response.blob();

      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      // Delay the page reload for 1 second (adjust as needed)
      setTimeout(() => {
        window.location.reload();
      }, 1000);
    } else {
      console.error("Error downloading file:", response.statusText);
      window.location.reload();
    }
  } catch (error) {
    // Check for ConnectionResetError and handle it
    if (error instanceof DOMException && error.message.includes('Connection is aborted')) {
      console.warn("Connection was aborted, possibly due to the user canceling the download.");
    } else {
      console.error("Error downloading file:", error);
      window.location.reload();
    }
  }
}
