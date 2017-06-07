var zdVote = function(settings){
    l = function(s) {
            console.log(s)
    };
    
    var css_class = '.'+settings.class;
    var ul = $(css_class);
   
   
    getCookie = function getCookie(name) {
      var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
      ));
      return matches ? decodeURIComponent(matches[1]) : undefined;
    }   
 
 
    setCookie = function setCookie(name, value, options) {
      options = options || {};
    
      var expires = options.expires;
    
      if (typeof expires == "number" && expires) {
        var d = new Date();
        d.setTime(d.getTime() + expires * 1000);
        expires = options.expires = d;
      }
      if (expires && expires.toUTCString) {
        options.expires = expires.toUTCString();
      }
    
      value = encodeURIComponent(value);
    
      var updatedCookie = name + "=" + value;
    
      for (var propName in options) {
        updatedCookie += "; " + propName;
        var propValue = options[propName];
        if (propValue !== true) {
          updatedCookie += "=" + propValue;
        }
      }
    
      document.cookie = updatedCookie;
    }   
   
   
    buildUl = function(){
        l('Building'+settings.count);
        for(var i=1; i<=settings.count; i++) {
                li = '<li data-score="'+i+'" class="glyphicon glyphicon-star-empty"></li>';
                ul.append(li)
             
            }    
    };
    
    
    hoverSiblings = function(el){
        el.prevAll().removeClass("glyphicon-star-empty");
        el.prevAll().addClass("glyphicon-star");         
    };
    
    unhoverSiblings = function(el){
        
        el.prevAll().removeClass("glyphicon-star");
        el.prevAll().addClass("glyphicon-star-empty");         
            
    };     
    
    onHover = function(){
            ul.on("mouseover","li",function(){
            
                $(this).removeClass("glyphicon-star-empty");
                $(this).addClass("glyphicon-star");
                hoverSiblings($(this));
            });
            
            ul.on("mouseout","li",function(){
            
                $(this).removeClass("glyphicon-star");
                $(this).addClass("glyphicon-star-empty");   
                unhoverSiblings($(this));
            });
            
            success = function(data){
                dt = data.split('|');
                l($('#zd_vote_'+dt[2]));
                $('#zd_vote_'+dt[2]).replaceWith('<p class="zd_vote">Проголосовало: '+dt[0]+', cредний бал: '+dt[1]+'</p>');

            };
            
            ul.on("click","li",function(e){
                e.preventDefault();
                var id = '#vote-'+$(e.target).parent().attr('data-id');
                var idel = $(e.target).parent().attr('data-id');
                $(id).show();
                var score = $(e.target).attr('data-score');
                $(id).click(function(e){
                    e.preventDefault();
                    $(id).hide();
                    var data = settings;
                    data.score = score
                    data.id =idel
                    cn = 'zd-vote-'+ data.id;
                    if(getCookie(cn)==1) {
                        data.voted = true;
                    } else {
                        setCookie(cn,1,{expires: 3600});
                        data.voted = false;
                    }
                    $.ajax({
                        type: "POST",
                        url: settings.url,
                        data: data,
                        success: success
                      });
                    
                });
                
            });
            
            /*
            ul.on("click","li",function(el){
                $('.zd_title').show();
                var data = settings;
                data.score = $(el.target).attr('data-score');
                data.id = $(el.target).parent().attr('data-id');
                cn = 'zd-vote-'+ data.id;
                if(getCookie(cn)==1) {
                    data.voted = true;
                } else {
                    setCookie(cn,1,{expires: 3600});
                    data.voted = false;
                }
                $.ajax({
                    type: "POST",
                    url: settings.url,
                    data: data,
                    success: success
                  });
            });
            */
            
    };
    
    return {
        activate: function(){
          
            buildUl();
            onHover();
        }
    }
    
}