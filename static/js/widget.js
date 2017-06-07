 $(document).ready(function(){
    
          /// hiligth dates
          
          $('#wg_content .number').each(function(item){
               var el = this;
               $('#wg_content .film_item').each(function(){
                    var nd = parseInt($(this).attr('data-day'));
                    var day = parseInt($(el).attr('data-id'));
                    
                    if (nd==day) {
                         $(el).addClass('red');
                    }
               });
               
                    
          });
    
      $("#wg_content .number").click(function(evt){
         evt.preventDefault();
         $('#wg_content li').removeClass('active');
         $('#wg_content .item').removeClass('active');
         $(evt.target).addClass('active');
         activate_tab();
         return false;
      });
      
      activate_tab = function(){
        var indx =  $('#wg_content li.active').attr("data-id");
        
        $('#item-'+indx).addClass('active');
        
      }
    
      $("#wg_content .arrow").click(function(evt){
             evt.preventDefault();
             var clicked = $(evt.target);
             
             if(clicked.hasClass('arrow_forward')){
                var nxt = $('#wg_content li.active').next();
                 
                if(nxt.hasClass('number')){
                    $('#wg_content li').removeClass('active');
                    $('#wg_content .item').removeClass('active');
                    nxt.click();
                    activate_tab();
                }             
             }
             
             if(clicked.hasClass('arrow_backward')){
                var prev = $('#wg_content li.active').prev();
                if(prev.hasClass('number')){
                    $('#wg_content li').removeClass('active');
                    $('#wg_content .item').removeClass('active');
                    prev.click();
                    activate_tab();
                }                        
             }             
            
        
        });       
    
 });