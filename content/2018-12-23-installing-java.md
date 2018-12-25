Title: How to Install Java  
Date: 2018-12-23 1:30 PM
Category: Spark

![Java Meme](/images/2018-12-23/java-meme.jpg){:width=500px}

#### Download & Install Java
Download & Install [Java Development Kit 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).
To figure out which version of Java I need to download, I check my windows
version by entering the following in a command prompt:
```
cmd> wmic os get osarchitecture
```
The output tells me I'm using the 64 bit version of Windows.  
```
OSArchitecture
64-bit
```
Download the Java version for your version of Windows. The Windows x86 and x64
versions of Java are respectively for the 32 and 64 bit edition of Windows. [Why is the 32 bit version of Windows called x86?](https://stackoverflow.com/questions/29974425/why-is-windows-32-bit-called-windows-x86-and-not-windows-x32)
<p style="float: left; font-size: 9pt; text-align: center; width: 98%;
margin-right: 1%; margin-bottom: 0.5em;">
<img src="/images/2018-12-23/java-install.PNG" alt="Java Download"
style="width: 100%" border="2">
Java Download Page</p>
#### Check that your JAVA_HOME environment variable is set  
```
cmd> echo %JAVA_HOME%
```
If you get something like the following, your JAVA_HOME environment variable is
set:  
```
C:\Program Files\Java\jdk1.8.0_191
```

If you get this, your JAVA_HOME environment variable is not set:  
```
:::bash
%JAVA_HOME%
```
### To set JAVA_HOME & add JAVA_HOME to PATH
Find where Java was installed on your computer. By default, Java is installed
in the `C:\Program Files (x86)\Java` or `C:\Program Files\Java` directory.
`JAVA_HOME` needs to point to your root Java directory. The `PATH` should
contain `JAVA_HOME\bin`. For me, I used the following to set my `JAVA_HOME`
environment variable and add `JAVA_HOME` to my `PATH`.  
```
cmd> setx JAVA_HOME "C:\Program Files\Java\jdk1.8.0_191"
cmd> setx PATH "%JAVA_HOME%\bin;%PATH%"
```  
Close your command prompt and reopen a new one to refresh your environment
variables. Verify that your `JAVA_HOME` and `PATH` were set correctly. Verify
that Java was installed correctly. 
```
:::text
cmd> echo %JAVA_HOME%
// to pretty print PATH
cmd> for %a in ("%path:;=";"%") do @echo %~a
cmd> java -version
```
You should see something like the following output:  
```
C:\Program Files\Java\jdk1.8.0_191
// this should appear somewhere in your PATH
C:\Program Files\Java\jdk1.8.0_191\bin
java version "1.8.0_191"
```
