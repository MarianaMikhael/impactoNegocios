/*------------------------------Navbar, transparente => sólido------------------------------*/
jQuery(function () {
    jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > 50) {
            $("#navbar-default").css('background-color', 'rgb(27, 38, 49)');
        } else {
            $("#navbar-default").css('background-color', 'rgba(27, 38, 49, 0.7)');
        }
    });
});

/*----------------------------------Formulário de Cadastro----------------------------------*/
$(function(){
    var atual_fs, next_fs, prev_fs;

    /*--------------------Barra de progress, próximo--------------------*/
    $('.next').click(function(){
        atual_fs = $(this).parent();
        next_fs = $(this).parent().next();

        $('#progress li').eq($('fieldset').index(next_fs)).addClass('ativo');
        atual_fs.hide(800);
        next_fs.show(800);
    });

    /*--------------------Barra de progress, anterior--------------------*/
    $('.prev').click(function(){
        atual_fs = $(this).parent();
        prev_fs = $(this).parent().prev();

        $('#progress li').eq($('fieldset').index(atual_fs)).removeClass('ativo');
        atual_fs.hide(800);
        prev_fs.show(800);
    });

});
