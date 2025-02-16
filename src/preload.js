// See the Electron documentation for details on how to use preload scripts:
// https://www.electronjs.org/docs/latest/tutorial/process-model#preload-scripts
const { contextBridge, ipcRenderer } = require ("electron");

contextBridge.exposeInMainWorld("electron", {
    sendPagesToPython: (pages) => ipcRenderer.send("run-python", pages),
    getEnv: () => ({
        USERNAME: process.env.OWN_USER 
    }),
    onPythonResponse: (callback) => ipcRenderer.on("python-response", (_, data) => callback(data))
});
