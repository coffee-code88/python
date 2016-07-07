function loadScript(url, type){
    console.log("Call script")
    if(type=="js"){
        var script=document.createElement("script")
        script.setAttribute("type", "text/javascript")
        script.setAttribute("src", url)
    }   
    else if(type=="css"){
        var script = document.createElement("link")
        script.setAttribute("rel", "stylesheet")
        script.setAttribute("type", "text/css")
        script.setAttribute("href", url)
    }
    if (typeof script != "undefined"){
        document.getElementsByTagName("head")[0].appendChild(script)
    }
}
