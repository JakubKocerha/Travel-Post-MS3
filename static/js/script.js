$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();
    $('.collapsible').collapsible(
        {
            inDuration: 400,
            outDuration: 400
        });
    $('.materialboxed').materialbox();
    $('#post_body').val('');
    M.textareaAutoResize($('#post_body'));
    $('input#title_text, input#title_text, textarea#summary, textarea#post_body').characterCounter();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        showClearBtn: true,
        i18n:{
            done: "Select"
        }
    });
});