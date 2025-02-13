window.addEventListener("DOMContentLoaded", () => {
    const button=document.getElementById('submitPages');
    button.addEventListener('click',()=>{
    let pages=document.getElementById('pageInput').value;
    if (pages) {
        // exec(`python main.py ${pages}`, (error, stdout, stderr) => {
        //     if (error) {
        //         console.error(`Error: ${error.message}`);
        //         return;
        //     }
        //     if (stderr) {
        //         console.error(`stderr: ${stderr}`);
        //         return;
        //     }
        //  console.log(stdout); // Output from Python script
            window.electron.sendPagesToPython(pages);
            alert("Pixela graph updated successfully!");
    } 
    else {
        alert("Please enter a valid number of pages.");
    }
    })
})