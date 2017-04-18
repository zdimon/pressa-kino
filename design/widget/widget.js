 $(document).ready(function(){
    
    
      $("#wg_content .number").click(function(evt){
         $('#wg_content li').removeClass('active');
         $(evt.target).addClass('active');
      }); 
    
      $("#wg_content .arrow").click(function(evt){
        
            
             if($(evt.target).hasClass('arrow_forward')){
                var nxt = $('#wg_content li.active').next();
                
                if(nxt.hasClass('number')){
                    $('#wg_content li').removeClass('active');
                    nxt.click();
                }
                
                
             }
             
             if($(evt.target).hasClass('arrow_backward')){
                var prev = $('#wg_content li.active').prev();
                if(prev.hasClass('number')){
                    $('#wg_content li').removeClass('active');
                    prev.click();
                }                
                           
                
             }             
            
        
        });       
    
 });