$( document ).ready(function(){

    $("#Button1").click(function() {

       $.mobile.changePage("#Seite2", {
           transition: "fade",
           changeHash: false
       });
   });
   
    $("#Button2").click(function(){
        $.mobile.changePage("#Seite1",{
            transition: "slide",
            changeHash: false
        });
    });
    
    $("#exampleLink").click(function(){
        $.mobile.changePage("#Seite3", {
            transition: "slide"
        });
    });

    $("#back").click(function(){
        $.mobile.changePage("#Seite2", {
            transition: "slide"
        });
    });
});
