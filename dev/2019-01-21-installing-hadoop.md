Title: How to install Hadoop on your computer
Date: 2019-01-12 2:35 PM
Category: Spark  

## Introduction  
This post is about installing Hadoop on a computer running Windows 10.  

To follow along with this post, you should already have Java (JDK 8) on your
machine.  

If you need help with those things, here are some helpful links:  

[How to Install Java (JDK 8)](../../23/how-to-install-java)  

### What is Hadoop?  
Hadoop is a framework that allows for the distributed processing of large data
sets across clusters of computers.

## Step 1 - Install Java  
#### Java Development Kit 8 (JDK 8) is already installed  
If JDK 8 is already installed on your machine skip to step 2.

#### How do I check if JDK 8 is installed on my machine?  
Open a windows command prompt and type the following:  

```
cmd> java -version  
```
If you get the following output:
```
java version "1.8.0_191"
```
then JDK 8 is installed on your machine. The first two numbers are the
important ones. The numbers after 1.8 are the build number and may vary
depending on your build.  

If you get an error, or a different version is installed, I recommend that you
download and install JDK 8.

## Step 2
#### Download Hadoop     
Download & Extract [Hadoop](https://hadoop.apache.org/releases.html). I chose
Hadoop version 2.9.2 which was the most recently updated Hadoop version at that
time. I downloaded the "Binary download" of Hadoop.

**Note**: Source releases must be compiled while binary releases are already
compiled. If you're using Windows, you'll often use the binary releases.  
[Install from source or binary?](https://stackoverflow.com/questions/5280906/difference-between-binary-release-and-source-release)  
**Note**: If you are getting a `Cannot create symbolic link` error, run your
extracting utility as Administrator.  
![Symbolic Link Error](/images/2019-01-12/symbolic-link-error.PNG)
[Cannot create symbolic link](https://superuser.com/questions/1076527/7zip-cannot-create-symbolic-link-access-is-denied-to-libhdfs-so-and-libhadoop-s)

### Step 3 - Add set HADOOP_HOME, Hadoop environment variables, and add to PATH  
Find where Hadoop was downloaded and extracted to your computer. Hadoop was
downloaded and extracted to my `Downloads` directory. `HADOOP_HOME` and other
Hadoop environment variables need to point to your root Hadoop directory. The
`PATH` should contain `HADOOP_HOME\bin`.  

I used the follow to set my `HADOOP_HOME`, other Hadoop environment variables,
and `PATH`.

```
cmd> setx HADOOP_HOME "C:\Users\echan\Downloads\hadoop-2.9.2"
cmd> setx HADOOP_MAPRED_HOME "C:\Users\echan\Downloads\hadoop-2.9.2"
cmd> setx HADOOP_COMMON_HOME "C:\Users\echan\Downloads\hadoop-2.9.2"
cmd> setx HADOOP_HDFS_HOME "C:\Users\echan\Downloads\hadoop-2.9.2"
cmd> setx YARN_HOME "C:\Users\echan\Downloads\hadoop-2.9.2"
cmd> setx HADOOP_CONF_DIR "C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop"
cmd> setx PATH "%HADOOP_HOME%\bin;%PATH%"
```
```
Close your command prompt and reopen a new one to refresh your environment
variables. Verify that your `SPARK_HOME` and `PATH` were set correctly.
```
:::text
cmd> echo %HADOOP_HOME%
cmd> echo %HADOOP_MAPRED_HOME%
cmd> echo %HADOOP_COMMON_HOME%
cmd> echo %HADOOP_HDFS_HOME%
cmd> echo %YARN_HOME%
cmd> echo %HADOOP_CONF_DIR%
// to pretty print PATH
cmd> for %a in ("%path:;=";"%") do @echo %~a
```
You should see something like the following output:  
```
// this should be the output for %HADOOP_HOME%, %HADOOP_MAPRED_HOME%, %HADOOP_COMMON_HOME%, %HADOOP_HDFS_HOME%, and %YARN_HOME%
C:\Users\echan\Downloads\hadoop-2.9.2
C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop
// this should appear somewhere in your PATH
C:\Users\echan\Downloads\hadoop-2.9.2\bin
```

```
cmd>   
```

![Python Kernel](/images/2018-12-26/python-kernel.PNG)

#### Execute Spark code!  
```
#!python  
import findspark
findspark.init()
import pyspark
sc = pyspark.SparkContext(appName = "myApp")
a = sc.parallelize(range(10))
a.collect()
```
![Python Kerenel](/images/2018-12-26/spark-python.PNG)

***Note - I tried doing this using Spark 2.4 and encountered the following
error: `Python worker failed to connect back`. I switched to Spark 2.3.2 and
was able to execute Spark code with no errors.***

## Spark - Scala
This step is to if you want to develop in Spark using Scala.  

#### Install spylon-kernel using pip  
Type the following in a command prompt:  
```
cmd> pip install spylon-kernel
```
#### Create a kernel spec
This allows us to select a Scala kerenel in a Jupyter Notebook.  
```
cmd> python -m spylon_kernel install
```
#### Open a Jupyter Notebook and select spylon-kernel.

![Spylon Kernel](/images/2018-12-26/spylon-kernel.PNG){:width=600px}
---
#### Execute Spark code!  
```
#!scala  
val a = sc.parallelize(1 to 9)
a.collect()
```
![Spark Scala](/images/2018-12-26/spark-scala.PNG){:width='600px'}  

***Note - I get a warning `Unable to load native-hadoop library for your platform...using
builtin-java classes where applicable`. This will be an issue if you connect to
a Hadoop cluster with Kerberos authentication but for our purposes, we can
ignore this.***

Happy developing!
