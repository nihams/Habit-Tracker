
window.addEventListener("DOMContentLoaded", () => {
    const envVars = window.electron.getEnv(); // Get environment variables
    console.log("Environment Variables:", envVars); // Debug log

    const button=document.getElementById('submitPages');
    const graphImg = document.getElementById("graph");
    const graphHeading = document.getElementById("graphHead")

    graphImg.style.display = "none"; 
    graphHeading.style.display = "none";

    button.addEventListener('click',()=>{
    let pages=document.getElementById('pageInput').value;
    if (pages) {
            window.electron.sendPagesToPython(pages);
            alert("Pixela graph updated successfully!");

            if (envVars.USERNAME) {
                graphImg.src = 
                    `https://pixe.la/v1/users/${envVars.USERNAME}/graphs/graph1`;
                graphImg.style.display = "block"; 
                graphHeading.style.display = "block";
            } else {
                console.error("USERNAME is missing!");
            }

            // window.electron.onPythonResponse((response) => {
            //     if (response.error) {
            //         alert("Failed to update Pixela graph: " + response.error);
            //     } else {
            //         alert("Pixela graph updated successfully!");
            //         document.getElementById("graph").src += ""; // Force refresh
            //     }
            // });
    } 
    else {
        alert("Please enter a valid number of pages.");
    }
    })
})