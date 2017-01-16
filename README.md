# [Guessblur](http://35.166.71.133/)
A game where you can't always trust your eyes! The user is displayed an image and they must decide whether the image is what the suggested description is.


###Inception
Guessblur was originally known as Fiddy, which was originally known as Fifty/Fifty. Based on Reddit's /r/FiftyFifty subreddit game, Guessblur was initially inteded to be a game where you select which of two differing options and live with the consequences. However, Reddit's /r/FiftyFifty is rooted heavily in unattractive NSFW options, so we had to rethink our angle. Instead we opted to develop an app based on /r/MisleadingThumbnails, and that became Guessblur.

  **The Rules:**

  _In Guessblur, you are given one of two possible descriptions of an image. You select whether or not you believe this is the   correct description of the image. You either gain a point or you don't. The only real rule is that you don't look at the
  source code because then it's pretty obvious which is the correct choice and then you're not very much fun._
***

###Making the Magic Happen
The biggest initial challenge was deciding how we'd arrange gameplay. Once we decided that we would be unable to do the FiftyFifty-based game, we realized utilizing an API to pull the images from reddit itself would be futile lest we were bombarded with images of dismembered humans. Plan B.

Upon realizing that MisleadingThumbnails could potentially take its place, we began digging. Imgur's API is surprisingly extensive, so it lended itself pretty generously to our project. Our MVP (minimum viable product) was an app that pulled options from a database of manually stored images and gave you one with a blur overlay, and Imgur's API allowed us to kind of take that a bit further. Thanks Imgur!
***

###The Hurdles
Sorting out the ins and outs of gameplay was definitely a challenge. A lot of staring into space and imagining syntax options that don't exist. Ultimately, Marvin came through with the functions that made it all function and we were able to get this show on the road. Also, opting to use pure CSS was a ballsy choice, but it was one that had a few happy benefits like... uh, get back to you on that in a bit.

> Nedra: Dear god, the CSS. It was so brutal. So brutal. I thought of every ex. I texted 2 of them. I still didn't get the CSS perfect, but I got some closure. It's raining. It's also 4am. I'm approaching 700 lines of CSS; is this normal?

####Guessblur in its many stages + Some lovely little errors:
<img src="http://i.imgur.com/XRvSLf3.png" alt="alt text" width="gameplay" height="100"> <img src="http://i.imgur.com/M20luVx.png" alt="alt text" width="gameplay" height="100"> <img src="http://i.imgur.com/4ibltWS.png" alt="alt text" width="gameplay" height="100"> <img src="https://raw.githubusercontent.com/DigitalCrafts-HTX-11-2016-Cohort/guessblur/master/static/gameplay.png" alt="alt text" width="gameplay" height="100"> 
***

###Screenshots
<img src="http://i.imgur.com/BIFspRo.png" alt="alt text" width="gameplay" height="100"> 
<img src="http://i.imgur.com/PX5GRzA.png" alt="alt text" width="gameplay" height="100"> 
<img src="http://i.imgur.com/Ur0agwu.png" alt="alt text" width="gameplay" height="100">

***

Built with ![heart](http://i.imgur.com/4PataBu.png) with:
HTML, Python, [soooo much] CSS, Flask, Jinja, JSON, [a wee bit of] Javascript
