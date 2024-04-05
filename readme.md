<h2 align="left">iDoom Guide Beta</h2>

###
iDoom is a brute force for url parameters, it can check whether a page returned content or not,
it is similar to a directory bruteforce, but it only works with Url parameters, a good example is a
code that references some content within the page.

Currently idoom is in beta version, but is being updated frequently, it is available for Linux, but we are already working on a version for Windows with the change of some libraries.

We are working on documentation that will soon be made available here.

<h2 align="left">Installing</h2>

###
To install just use these commands in the Linux terminal

    cd Desktop
    git clone https://github.com/usuario/repositorio
    

<h2 align="left">Running</h2>

###

you need to know a few things before running idoom , first you need to have a target URL.

    https://example/files.php?&r=27627324326356306&cd=5057&cd2=29
    
  <h2 align="left">Preparing URL</h2>

###  

After you have collected a target url, you need to prepare this url and separate which parameter you will use, like this:

        https://example/files.php?&r=27627324326356306&cd=5057
        
        &cd2=
Remember, this script is a brute force, if this were a real case, the brute force would be applied to the parameter &cd2= , you can use whatever parameter you want from the URL, as long as it doesn't change the query logic!
