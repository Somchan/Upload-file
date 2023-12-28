document.addEventListener("DOMContentLoaded", function () {
    // Add click event listener to the "Delete All" button
    const deleteAllButton = document.getElementById("delete-all");
    deleteAllButton.addEventListener("click", deleteAllFiles);
});

async function deleteAllFiles() {
    if (confirm('Are you sure you want to delete all files?')) {
        try {
            // Simulate API call to delete all files
            const response = await fetch('http://${process.env.HOST_PC}:${process.env.PORT}/api/delete-all', {
                method: 'DELETE',
            });

            if (response.ok) {
                console.log('All files deleted successfully.');
                // Perform any UI update or refresh if needed
            } else {
                console.error('Error deleting all files:', response.statusText);
            }
        } catch (error) {
            console.error('Error deleting all files:', error);
        }
    }
    window.location.reload();
}