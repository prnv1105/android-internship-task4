function notify(){
    let toast = document.createElement("div");
    toast.innerText = "🚀 System Activated!";
    
    toast.style.position = "fixed";
    toast.style.bottom = "30px";
    toast.style.right = "30px";
    toast.style.background = "rgba(0,0,0,0.7)";
    toast.style.color = "#00f2fe";
    toast.style.padding = "15px";
    toast.style.borderRadius = "10px";
    toast.style.boxShadow = "0 0 15px #00f2fe";

    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 3000);
}