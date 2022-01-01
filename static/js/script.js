$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();
    $('.collapsible').collapsible(
        {
            inDuration: 400,
            outDuration: 400
        });
    $('.materialboxed').materialbox();
});