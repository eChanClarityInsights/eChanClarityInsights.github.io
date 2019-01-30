Title: How to install Hadoop on your computer
Date: 2019-01-30 8:04 AM
Category: Hadoop   

## Introduction  
This post is about installing Hadoop on a computer running Windows 10.  

### What is Hadoop?  
Hadoop is a framework that allows for distributed processing of large data sets
across clusters of computers.  

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
then JDK 8 is installed on your machine and your `JAVA_HOME` environment
variable is set. The first two numbers of the version number are the important
ones. The numbers after 1.8 are the build number and may vary depending on your
build.  

If you get an error, or a different version is installed, I recommend that you
download and install JDK 8.  

If you need help with that, here is a helpful link:  

[How to Install Java (JDK 8)](../../23/how-to-install-java)  

## Step 2 - Download Hadoop     
Download & Extract [Hadoop](https://hadoop.apache.org/releases.html). I chose
Hadoop version 2.9.2 which was the most recently updated Hadoop version at that
time. I downloaded the "Binary download" of Hadoop.

**Note**: If you're using Windows, I recommend to use the binary releases.
Binary releases are already compiled while source releases must be compiled.   
To read more: [Install from source or binary?](https://stackoverflow.com/questions/5280906/difference-between-binary-release-and-source-release)  
**Note**: If you are getting a `Cannot create symbolic link` error, run your
extracting utility as Administrator.  
![Symbolic Link Error](/images/2019-01-12/symbolic-link-error.PNG)  
To read more: [Cannot create symbolic link](https://superuser.com/questions/1076527/7zip-cannot-create-symbolic-link-access-is-denied-to-libhdfs-so-and-libhadoop-s)

## Step 3 - Set HADOOP_HOME, Hadoop environment variables, and add to PATH  
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

Close your command prompt and reopen a new one to refresh your environment
variables. Verify that your environment variables were set correctly.  

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
// this should be the output for %HADOOP_CONF_DIR  
C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop
// this should appear somewhere in your PATH
C:\Users\echan\Downloads\hadoop-2.9.2\bin
```

## Step 4 - Set properties and variables for xml files  
Find the file `core-site.xml`. For me, it is located at `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\core-site.xml`.
Add the following property inside of the configuration tag:
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
Find the file `mapred-site.xml.template`. For me, it is located at `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\mapred-site.xml.template`.
Rename this file `mapred-site.xml` and add the following property inside of the
configuration tag:  
```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```  

#### Create data, datanode, and namenode directories  
Navigate to your root Hadoop directory. For me that is `C:\Users\echan\Downloads\hadoop-2.9.2`.
Create the following directories:  
- `C:\Users\echan\Downloads\hadoop-2.9.2\data`  
- `C:\Users\echan\Downloads\hadoop-2.9.2\data\datanode`  
- `C:\Users\echan\Downloads\hadoop-2.9.2\data\namenode`  

Find the file `hdfs-site.xml`. For me, it is located at `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\hdfs-site.xml`.
Add the following property inside of the configuration tag:  
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/Users/echan/Downloads/hadoop-2.9.2/etc/hadoop/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/Users/echan/Downloads/hadoop-2.9.2/etc/hadoop/datanode</value>
    </property>
</configuration>
```
***Note*** Notice two things in this configuration:  
- I didn't specify `C:` when specifying the path to the namenode and data directories.  
- I used forward slashes (`/`) when specifying my path.  
To read more: [NameNode failed to start](https://stackoverflow.com/questions/34871814/failed-to-start-namenode-in-hadoop)

Find the file `yarn-site.xml`. For me, it is located at `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\yarn-site.xml`
Add the following property inside of the configuration tag:  
```
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>  
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
</configuration>
```   
Open a command prompt navigate to the directory where your `JAVA_HOME` is
located. We are going to convert our `JAVA_HOME` from a long path to a windows
short name.
```
cmd>cd %JAVA_HOME%  
cmd>for %I in (.) do echo %sI
```
You should see something like this:
```
cmd>C:\PROGRA~1\Java\JDK18~1.0_1
```
Find the file `hadoop-env.cmd`. For me, it is located at `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\hadoop-env.cmd`.
Set the `JAVA_HOME` variable in `hadoop-env.cmd` to your windows short name
`JAVA_HOME` path.
```
set JAVA_HOME=C:\PROGRA~1\Java\JDK18~1.0_1
```

## Step 5 - Download Hadoop configuration
Download the following [Hadoop Configuration.zip](https://github.com/MuhammadBilalYar/HADOOP-INSTALLATION-ON-WINDOW-10/blob/master/Hadoop%20Configuration.zip)   
Delete the bin directory inside your Hadoop root directory and replace it with
the new bin directory downloaded and extracted from [Hadoop Configuration.zip](https://github.com/MuhammadBilalYar/HADOOP-INSTALLATION-ON-WINDOW-10/blob/master/Hadoop%20Configuration.zip).
For me, I deleted my `C:\Users\echan\Downloads\hadoop-2.9.2\bin\` directory and
replaced it with the newly unzipped `bin` directory.

## Step 6 - Format the NameNode  
Type the following in your command prompt to format the NameNode:  
```
cmd>hdfs namenode -format
```  
The following message popped up when I did this:  
```
Re-format filesystem in Storage Directory C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\namenode ? (Y or N)
```  
This happens when `dfs.namenode.name.dir` already exists. Re-formating it will
delete the existing metadata. I chose `Y`.
To read more: [Re-format filesystem in Storage Directory?](https://stackoverflow.com/questions/42803137/query-on-hadoop-namenode-format-command)  

Scrolling through the install log, I received the following warning:
```
WARN common.Util: Path /Users/echan/Downloads/hadoop-2.9.2/etc/hadoop/namenode should be specified as a URI in configuration files. Please update hdfs configuration.
```
This warning was fixed in subsequent versions and I ignored it for this
installation. Read more about it here: [Name Node Format Warning](https://stackoverflow.com/questions/37280383/hadoop-name-node-format-warning)

## Step 7 - Run start-dfs.cmd & start-yarn.cmd  
Open a command prompt and navigate to the `sbin` directory. For me this is `C:\Users\echan\Downloads\hadoop-2.9.2\sbin\`
and type the following to start the NameNode and one DataNode:  
```
cmd>start-dfs.cmd
```
Open a separate command prompt, navigate to the `sbin` directory and type the
following to start yarn resourcemanager and nodemanager:  
```
cmd>start-yarn.cmd
```
***Note*** The first time I ran this, I received an error In the resourcemanager
command prompt, I got the following error:
```
FATAL resourcemanager.ResourceManager: Error starting ResourceManager
java.lang.NoClassDefFoundError: org/apache/hadoop/yarn/server/timelineservice/collector/TimelineCollectorManager
```
To fix this, I copied the timelineservice jar
`hadoop-yarn-server-timelineservice-2.9.2.jar` from the
`C:\Users\echan\Downloads\hadoop-2.9.2\share\hadoop\yarn\timelineservice`
directory to `C:\Users\echan\Downloads\hadoop-2.9.2\share\hadoop\yarn` directory.  

Run the `start-yarn.cmd` command again and this time yarn resourcemanager
started successfully!

To read more: [No Class Found: timelineservice collector](https://stackoverflow.com/questions/51118358/noclassdeffounderror-org-apache-hadoop-yarn-server-timelineservice-collector-tim)

Navigate to http://localhost:8088 browse the Hadoop UI.   
The web interface for the NameNode is available at http://localhost:50070  

## Step 8 - Create a directory and put a file on Hadoop  
Type the following in your command prompt to create a few directories:  
```
// create a directory for all users    
cmd>hadoop fs -mkdir /user  
// create a directory for a specific user, for me I typed hadoop fs -mkdir /user/echan
cmd>hadoop fs -mkdir /user/<username>
// put a file into user directory, for my I typed hadoop fs -put test.txt /user/echan
// hadoop fs -put <path to local file> <path to hadoop directory>
cmd>hadoop fs -put test.txt /user/echan
// check that your file got put into your hdfs directory
cmd>hadoop fs -ls /user/echan
```
## Debugging: Fixing Incompatible cluster IDs  
I ran into the following problem in my Name Node:  
```
WARN org.apache.hadoop.hdfs.server.common.Storage: java.io.IOException: Incompatible clusterIDs
org.apache.hadoop.hdfs.server.datanode.DataNode: Initialization failed for Block pool
```  
To fix this, I copied the CluserID value from my `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\namenode\current\VERSION` file
file to the `C:\Users\echan\Downloads\hadoop-2.9.2\etc\hadoop\datanode\current\VERSION` file.
To read more: [Incompatible cluster IDs](https://stackoverflow.com/questions/35108445/java-io-ioexception-incompatible-clusterids)  

Happy developing!
