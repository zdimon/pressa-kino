 $(document).ready(function(){
    
    
      $("#wg_content .number").click(function(evt){
         $('#wg_content li').removeClass('active');
         $('#wg_content .item').removeClass('active');
         $(evt.target).addClass('active');
         activate_tab();
      });
      
      activate_tab = function(){
        var indx =  $('#wg_content li.active').index();
        $('#item-'+indx).addClass('active');
        
      }
    
      $("#wg_content .arrow").click(function(evt){
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