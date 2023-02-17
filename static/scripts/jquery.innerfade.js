/* =========================================================

// jquery.innerfade.js

// Datum: 2008-02-14
// Firma: Medienfreunde Hofmann & Baldes GbR
// Author: Torsten Baldes
// Mail: t.baldes@medienfreunde.com
// Web: http://medienfreunde.com

// based on the work of Matt Oakes http://portfolio.gizone.co.uk/applications/slideshow/
// and Ralf S. Engelschall http://trainofthoughts.org/

*
*  <ul id="news"> 
*      <li>content 1</li>
*      <li>content 2</li>
*      <li>content 3</li>
*  </ul>
*  
*  $('#news').innerfade({ 
*	  animationtype: Type of animation 'fade' or 'slide' (Default: 'fade'), 
*	  speed: Fading-/Sliding-Speed in milliseconds or keywords (slow, normal or fast) (Default: 'normal'), 
*	  timeout: Time between the fades in milliseconds (Default: '2000'), 
*	  type: Type of slideshow: 'sequence', 'random' or 'random_start' (Default: 'sequence'), 
*	  containerheight: Height of the containing element in any css-height-value (Default: 'auto'),
*	  runningclass: CSS-Class which the container get’s applied (Default: 'innerfade'),
*	  children: optional children selector (Default: null)
*  }); 
*

// ========================================================= */


function removeFilter(e){if(e.style.removeAttribute){e.style.removeAttribute("filter")}}(function(e){e.fn.innerfade=function(t){return this.each(function(){e.innerfade(this,t)})};e.innerfade=function(t,n){var r={animationtype:"fade",speed:"normal",type:"sequence",timeout:2e3,containerheight:"auto",runningclass:"innerfade",children:null};if(n)e.extend(r,n);if(r.children===null)var i=e(t).children();else var i=e(t).children(r.children);if(i.length>1){e(t).css("position","relative").css("height",r.containerheight).addClass(r.runningclass);for(var s=0;s<i.length;s++){e(i[s]).css("z-index",String(i.length-s)).css("position","absolute").hide()}if(r.type=="sequence"){setTimeout(function(){e.innerfade.next(i,r,1,0)},r.timeout);e(i[0]).show()}else if(r.type=="random"){var o=Math.floor(Math.random()*i.length);setTimeout(function(){do{u=Math.floor(Math.random()*i.length)}while(o==u);e.innerfade.next(i,r,u,o)},r.timeout);e(i[o]).show()}else if(r.type=="random_start"){r.type="sequence";var u=Math.floor(Math.random()*i.length);setTimeout(function(){e.innerfade.next(i,r,(u+1)%i.length,u)},r.timeout);e(i[u]).show()}else{alert("Innerfade-Type must either be 'sequence', 'random' or 'random_start'")}}};e.innerfade.next=function(t,n,r,i){if(n.animationtype=="slide"){e(t[i]).slideUp(n.speed);e(t[r]).slideDown(n.speed)}else if(n.animationtype=="fade"){e(t[i]).fadeOut(n.speed);e(t[r]).fadeIn(n.speed,function(){removeFilter(e(this)[0])})}else alert("Innerfade-animationtype must either be 'slide' or 'fade'");if(n.type=="sequence"){if(r+1<t.length){r=r+1;i=r-1}else{r=0;i=t.length-1}}else if(n.type=="random"){i=r;while(r==i)r=Math.floor(Math.random()*t.length)}else alert("Innerfade-Type must either be 'sequence', 'random' or 'random_start'");setTimeout(function(){e.innerfade.next(t,n,r,i)},n.timeout)}})(jQuery)

// **** Apply the fade settings ****

$(document).ready(function() {
    $('#rotation').innerfade({
        animationtype: 'fade',
        speed: 750,
        type: 'sequence',
        timeout: 3000,
        containerheight: 'auto',
        runningclass: 'innerfade',
        children: null
    });
});