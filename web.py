#coding=utf-8
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #return '<h1>Hello, web!</h1>'
    return """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head profile="http://gmpg.org/xfn/11">

<meta http-equiv="content-type" content="text/html; charset=UTF-8" />

<title>Goagent Iplist 未被干扰可用Google IP汇总 - Learning Notes</title>



<!-- 使用url函数转换相关路径 -->

<link rel="stylesheet" type="text/css" media="all" href="https://cb.e-fly.org/usr/themes/default/style.css" />



<!-- 通过自有函数输出HTML头部信息 -->

<meta name="description" content="不定时更新.分享Google可用IP段汇总如下,以方便大家查询使用.更新IP的初衷是为了让各位有学习需求的朋友可以方便的浏览.希望各位朋友减少浏览不必要的各类网站,减小IP被封几率.

每次更新的IP..." />
<meta name="keywords" content="Goagent,翻墙,iplist" />
<meta name="generator" content="Typecho 0.9/13.12.12" />
<meta name="template" content="default" />
<link rel="pingback" href="https://cb.e-fly.org/action/xmlrpc" />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://cb.e-fly.org/action/xmlrpc?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://cb.e-fly.org/action/xmlrpc?wlw" />
<script type="text/javascript">
//<![CDATA[
var TypechoComment = {
    dom : function (id) {
        return document.getElementById(id);
    },
    
    create : function (tag, attr) {
        var el = document.createElement(tag);
        
        for (var key in attr) {
            el.setAttribute(key, attr[key]);
        }
        
        return el;
    },

    reply : function (cid, coid) {
        var comment = this.dom(cid), parent = comment.parentNode,
            response = this.dom('respond-post-270'), input = this.dom('comment-parent'),
            form = 'form' == response.tagName ? response : response.getElementsByTagName('form')[0],
            textarea = response.getElementsByTagName('textarea')[0];

        if (null == input) {
            input = this.create('input', {
                'type' : 'hidden',
                'name' : 'parent',
                'id'   : 'comment-parent'
            });

            form.appendChild(input);
        }
        
        input.setAttribute('value', coid);

        if (null == this.dom('comment-form-place-holder')) {
            var holder = this.create('div', {
                'id' : 'comment-form-place-holder'
            });
            
            response.parentNode.insertBefore(holder, response);
        }

        comment.appendChild(response);
        this.dom('cancel-comment-reply-link').style.display = '';
        
        if (null != textarea && 'text' == textarea.name) {
            textarea.focus();
        }
        
        return false;
    },

    cancelReply : function () {
        var response = this.dom('respond-post-270'),
        holder = this.dom('comment-form-place-holder'), input = this.dom('comment-parent');

        if (null != input) {
            input.parentNode.removeChild(input);
        }

        if (null == holder) {
            return true;
        }

        this.dom('cancel-comment-reply-link').style.display = 'none';
        holder.parentNode.insertBefore(response, holder);
        return false;
    }
}
//]]>
</script></head>



<body>

<div id="header" class="container_16 clearfix">

	<form id="search" method="post" action="/">

		<div><input type="text" name="s" class="text" size="20" /> <input type="submit" class="submit" value="Search" /></div>

    </form>

	<div id="logo">

	    <h1><a href="https://cb.e-fly.org/">

        Learning Notes        </a></h1>

	    <p class="description">一个IT人的笔记博客 , 用心将每一件简单的事情做到极致 .</p>

    </div>

</div><!-- end #header -->



<div id="nav_box" class="clearfix">

<ul class="container_16 clearfix" id="nav_menu">

    <li><a href="https://cb.e-fly.org/">Index</a></li>

    <li><a href="https://cb.e-fly.org/club/" title="Cubieboard Forum" target="_blank">Forum</a></li>

            <li><a href="https://cb.e-fly.org/system-info.html" title="Systeminfo">Systeminfo</a></li>

        <li><a href="https://cb.e-fly.org/cam.html" title="Timelapse">Timelapse</a></li>

        <li><a href="https://cb.e-fly.org/guestbook.html" title="Guestbook">Guestbook</a></li>

        <li><a href="https://cb.e-fly.org/start-page.html" title="About">About</a></li>

    </ul>

</div>



<div class="container_16 clearfix">

    <div class="grid_10" id="content">

        <div class="post">

			<h2 class="entry_title"><a href="https://cb.e-fly.org/archives/goagent-iplist.html">Goagent Iplist 未被干扰可用Google IP汇总</a></h2>

			<p class="entry_data">

				<span>Auther：Cannikin</span>

				<span>Date：December 13, 2014</span>

				Category：<a href="https://cb.e-fly.org/category/Security/">Security</a><br><br><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><!-- ad02 --><ins class="adsbygoogle" style="display:inline-block;width:468px;height:15px" data-ad-client="ca-pub-3035338775005434" data-ad-slot="3942174409"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

			</p>

			<p><html>

<head>

	<title></title>

</head>

<body>

<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><img alt="" src="/usr/uploads/2014/06/949278152.png" style="width: 525px; height: 216px;" /></div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;">不定时更新.分享Google可用IP段汇总如下,以方便大家查询使用.<br /><strong>更新IP的初衷是为了让各位有学习需求的朋友可以方便的浏览.<br />希望各位朋友减少浏览不必要的各类网站,减小IP被封几率.</strong></div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;">每次更新的IP列表,可能同一天变更多次，请以文章更新日期时间为准。<br />近期用户网络封锁情况各不相同，IP使用效果也不同，如果您的IP失效了，欢迎及时留言我。<br /><strong>另因地区差异，如果您的IP使用上无障碍就无须更新，最新的未必适应您的网络环境。</strong></div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/12/2814066189.txt" target="_blank">点此下载</a>(2014.12.13)&nbsp;<a href="/usr/uploads/2014/12/4061389382.txt" target="_blank">点此查看</a>(2014.12.11)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/12/1712056588.txt" target="_blank">点此查看</a>(2014.12.10)&nbsp;<a href="/usr/uploads/2014/12/4218324716.txt" target="_blank">点此查看</a>(2014.12.05)&nbsp;<a href="/usr/uploads/2014/12/848259993.txt" target="_blank">点此查看</a>(2014.12.03)&nbsp;<a href="/usr/uploads/2014/12/2169961824.txt" target="_blank">点此查看</a>(2014.12.02)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/12/2197132981.txt" target="_blank">点此查看</a>(2014.12.01)&nbsp;<a href="/usr/uploads/2014/11/128759119.txt" target="_blank">点此查看</a>(2014.11.28)&nbsp;<a href="/usr/uploads/2014/11/1352030046.txt" target="_blank">点此查看</a>(2014.11.26)&nbsp;<a href="/usr/uploads/2014/11/3020812015.txt" target="_blank">点此查看</a>(2014.11.24)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/11/1715282457.txt" target="_blank">点此查看</a>(2014.11.21)&nbsp;<a href="/usr/uploads/2014/11/1495687276.txt" target="_blank">点此查看</a>(2014.11.19)&nbsp;<a href="/usr/uploads/2014/11/1580991719.txt" target="_blank">点此查看</a>(2014.11.17)&nbsp;<a href="/usr/uploads/2014/11/996947349.txt" target="_blank">点此查看</a>(2014.11.15)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/11/2018033141.txt" target="_blank">点此查看</a>(2014.11.12)&nbsp;<a href="/usr/uploads/2014/11/3973554451.txt" target="_blank">点此查看</a>(2014.11.10)&nbsp;<a href="/usr/uploads/2014/11/2876093604.txt" target="_blank">点此查看</a>(2014.11.08)&nbsp;<a href="/usr/uploads/2014/11/248215181.txt" target="_blank">点此查看</a>(2014.11.06)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><span style="background-color: rgb(238, 238, 238);"><a href="/usr/uploads/2014/11/1732340933.txt" target="_blank">点此查看</a>(2014.11.04)&nbsp;</span><a href="/usr/uploads/2014/11/4109303794.txt" target="_blank">点此查看</a>(2014.11.01)&nbsp;<a href="/usr/uploads/2014/10/1537424289.txt" target="_blank">点此查看</a>(2014.10.30)&nbsp;<a href="/usr/uploads/2014/10/2109248342.txt" target="_blank">点此查看</a>(2014.10.29)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/10/3835954448.txt" target="_blank">点此查看</a>(2014.10.28)&nbsp;<a href="/usr/uploads/2014/10/2936347808.txt" target="_blank">点此查看</a>(2014.10.25)&nbsp;<a href="/usr/uploads/2014/10/1771617882.txt" target="_blank">点此查看</a>(2014.10.24)&nbsp;<a href="/usr/uploads/2014/10/2091729461.txt" target="_blank">点此查看</a>(2014.10.22)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/10/3384597577.txt" target="_blank">点此查看</a>(2014.10.14)&nbsp;<a href="/usr/uploads/2014/10/1416854676.txt" target="_blank">点此查看</a>(2014.10.11)&nbsp;<a href="/usr/uploads/2014/10/1565409578.txt" target="_blank">点此查看</a>(2014.10.08)&nbsp;<a href="/usr/uploads/2014/10/251013092.txt" target="_blank">点此查看</a>(2014.10.04)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/10/992750894.txt" target="_blank">点此查看</a>(2014.10.01)&nbsp;<a href="/usr/uploads/2014/09/309675296.txt" target="_blank">点此查看</a>(2014.09.28)&nbsp;<a href="/usr/uploads/2014/09/4112370767.txt" target="_blank">点此查看</a>(2014.09.24)&nbsp;<a href="/usr/uploads/2014/09/2759281199.txt" target="_blank">点此查看</a>(2014.09.23)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/09/2860881570.txt" target="_blank">点此查看</a>(2014.09.20)&nbsp;<a href="/usr/uploads/2014/09/3363052597.txt" target="_blank">点此查看</a>(2014.09.18)&nbsp;<a href="/usr/uploads/2014/09/2739495508.txt" target="_blank">点此查看</a>(2014.09.16)&nbsp;<a href="/usr/uploads/2014/09/3176322817.txt" target="_blank">点此查看</a>(2014.09.12)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/09/1855624818.txt" target="_blank">点此查看</a>(2014.09.10)&nbsp;<a href="/usr/uploads/2014/09/3613697811.txt" target="_blank">点此查看</a>(2014.09.08)&nbsp;<a href="/usr/uploads/2014/09/2311970684.txt" target="_blank">点此查看</a>(2014.09.06)&nbsp;<a href="/usr/uploads/2014/09/1019352673.txt" target="_blank">点此查看</a>(2014.09.01)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/08/3437884355.txt" target="_blank">点此查看</a>(2014.08.30)&nbsp;<a href="/usr/uploads/2014/08/1263115039.txt" target="_blank">点此查看</a>(2014.08.29)&nbsp;<a href="/usr/uploads/2014/08/2129599275.txt" target="_blank">点此查看</a>(2014.08.27)&nbsp;<a href="/usr/uploads/2014/08/2670701754.txt" target="_blank">点此查看</a>(2014.08.21)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/08/2577677952.txt" target="_blank">点此查看</a>(2014.08.19)&nbsp;<a href="/usr/uploads/2014/08/157337218.txt" target="_blank">点此查看</a>(2014.08.18)&nbsp;<a href="/usr/uploads/2014/08/910425125.txt" target="_blank">点此查看</a>(2014.08.15)&nbsp;<a href="/usr/uploads/2014/08/952903646.txt" target="_blank">点此查看</a>(2014.08.13)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/08/2193753812.txt" target="_blank">点此查看</a>(2014.08.10)&nbsp;<a href="/usr/uploads/2014/08/265749402.txt" target="_blank">点此查看</a>(2014.08.06)&nbsp;<a href="/usr/uploads/2014/08/2091610879.txt" target="_blank">点此查看</a>(2014.08.05)&nbsp;<a href="/usr/uploads/2014/08/341267097.txt" target="_blank">点此查看</a>(2014.08.03)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/08/3906425099.txt" target="_blank">点此查看</a>(2014.08.01)&nbsp;<a href="/usr/uploads/2014/07/622485433.txt" target="_blank">点此查看</a>(2014.07.29)&nbsp;<a href="/usr/uploads/2014/07/2248949376.txt" target="_blank">点此查看</a><span style="background-color: rgb(238, 238, 238);">(2014.07.26)&nbsp;</span><a href="/usr/uploads/2014/07/3280726612.txt" target="_blank">点此查看</a><span style="background-color: rgb(238, 238, 238);">(2014.07.25)</span></div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/07/4013986549.txt" target="_blank">点此查看</a>(2014.07.21)&nbsp;<a href="/usr/uploads/2014/07/1102643665.txt" target="_blank">点此查看</a>(2014.07.17)&nbsp;<a href="/usr/uploads/2014/07/3389753834.txt" target="_blank">点此查看</a>(2014.07.15)&nbsp;<a href="/usr/uploads/2014/07/157321242.txt" target="_blank">点此查看</a>(2014.07.10)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/07/1344046617.txt" target="_blank">点此查看</a>(2014.07.07)&nbsp;<a href="/usr/uploads/2014/07/11125476.txt" target="_blank">点此查看</a>(2014.07.04)&nbsp;<a href="/usr/uploads/2014/06/1535576661.txt" target="_blank">点此查看</a>(2014.06.29)&nbsp;<a href="/usr/uploads/2014/06/731874940.txt" target="_blank">点此查看</a>(2014.06.26)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/06/4125741737.txt" target="_blank">点此查看</a>(2014.06.22)&nbsp;<a href="/usr/uploads/2014/06/2596967765.txt" target="_blank">点此查看</a>(2014.06.20)&nbsp;<a href="/usr/uploads/2014/06/4243235728.txt" target="_blank">点此查看</a>(2014.06.17)&nbsp;<a href="/usr/uploads/2014/06/1292235460.txt" target="_blank">点此查看</a>(2014.06.16)</div>



<div style="background:#eee;border:1px solid #ccc;padding:5px 10px;"><a href="/usr/uploads/2014/06/2173448421.txt" target="_blank">点此查看</a>(2014.06.14)&nbsp;<a href="/usr/uploads/2014/06/2876807154.txt" target="_blank">点此查看</a>(2014.06.13)&nbsp;<a href="/usr/uploads/2014/06/4279876020.txt" target="_blank">点此查看</a>(2014.06.12)&nbsp;<a href="/usr/uploads/2014/06/1726718259.txt" target="_blank">点此查看</a>(2014.06.05)</div>

</body>

</html></p>			<p class="tags">Tags: <a href="https://cb.e-fly.org/tag/Goagent/">Goagent</a>, <a href="https://cb.e-fly.org/tag/%E7%BF%BB%E5%A2%99/">翻墙</a>, <a href="https://cb.e-fly.org/tag/iplist/">iplist</a></p>

		</div>



		<div id="comments">

                        			<h4>118 Comments &raquo;</h4>

            

            <ol class="page-navigator"><li class="current"><a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comments">1</a></li><li><a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-2#comments">2</a></li><li><a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-3#comments">3</a></li><li><a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-4#comments">4</a></li><li><span>...</span></li><li><a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-11#comments">11</a></li><li><a class="next" href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-2#comments">&raquo;</a></li></ol>            

            <ol class="comment-list"><li id="comment-449" class="comment-body comment-parent comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/7a872e2d534b686041d6972fbd25c88e?s=32&amp;r=X&amp;d=" alt="songtime" width="32" height="32" />        <cite class="fn">songtime</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-449">December 13th, 2014 at 04:58 am</a>
            </div>
    <div class="comment-content">
    <p>gogotester更新了,新版的2.0.3.7检测出来的IP,再进行下带宽测试,就得到了GAE可用IP.我之前从楼主这里获取过高质量IP,非常感谢楼主的劳动付出.<br>
现在高质量IP已经可以完全自动获取了.</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=449#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-449', 449);">回复</a>    </div>
    </li>
<li id="comment-446" class="comment-body comment-parent comment-even">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/e547e84b0bb933866d82848f0d2edcb7?s=32&amp;r=X&amp;d=" alt="badday" width="32" height="32" />        <cite class="fn">badday</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-446">December 10th, 2014 at 06:27 pm</a>
            </div>
    <div class="comment-content">
    <p>12.10电信基本阵亡，极少数存活的延迟极高</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=446#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-446', 446);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-447" class="comment-body comment-child comment-level-odd comment-odd comment-by-author">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/5eceb4876d630f1289e2b34a645903fd?s=32&amp;r=X&amp;d=" alt="Cannikin" width="32" height="32" />        <cite class="fn"><a href="https://www.e-fly.org" rel="external nofollow">Cannikin</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-447">December 11th, 2014 at 09:47 am</a>
            </div>
    <div class="comment-content">
    <p>已更新，感谢反馈。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=447#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-447', 447);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-448" class="comment-body comment-child comment-level-even comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/e547e84b0bb933866d82848f0d2edcb7?s=32&amp;r=X&amp;d=" alt="badday" width="32" height="32" />        <cite class="fn">badday</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-448">December 12th, 2014 at 10:11 am</a>
            </div>
    <div class="comment-content">
    <p>非常感谢您</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=448#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-448', 448);">回复</a>    </div>
    </li>
</ol>    </div>
    </li>
</ol>    </div>
    </li>
<li id="comment-445" class="comment-body comment-parent comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/3899c27d09daf9cb8f1bd8e3b0309bc8?s=32&amp;r=X&amp;d=" alt="quarrycrusher" width="32" height="32" />        <cite class="fn"><a href="http://www.51stonecrusher.net/stone-crusher/quarry-crusher.html" rel="external nofollow">quarrycrusher</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-445">December 10th, 2014 at 02:24 pm</a>
            </div>
    <div class="comment-content">
    <p>thank you very much for your share.</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=445#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-445', 445);">回复</a>    </div>
    </li>
<li id="comment-443" class="comment-body comment-parent comment-even">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/00dafc6798af91c535623598c2d2176a?s=32&amp;r=X&amp;d=" alt="NOm" width="32" height="32" />        <cite class="fn">NOm</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-443">December 9th, 2014 at 10:24 pm</a>
            </div>
    <div class="comment-content">
    <p>12月5日的IP好像也被联通屏蔽了。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=443#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-443', 443);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-444" class="comment-body comment-child comment-level-odd comment-odd comment-by-author">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/5eceb4876d630f1289e2b34a645903fd?s=32&amp;r=X&amp;d=" alt="Cannikin" width="32" height="32" />        <cite class="fn"><a href="https://www.e-fly.org" rel="external nofollow">Cannikin</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-444">December 10th, 2014 at 09:54 am</a>
            </div>
    <div class="comment-content">
    <p>已更新，感谢反馈。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=444#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-444', 444);">回复</a>    </div>
    </li>
</ol>    </div>
    </li>
<li id="comment-439" class="comment-body comment-parent comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/13fe3c1d0a0e692bc81226c99418834d?s=32&amp;r=X&amp;d=" alt="rurgieo" width="32" height="32" />        <cite class="fn">rurgieo</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-439">December 8th, 2014 at 04:07 pm</a>
            </div>
    <div class="comment-content">
    <p>博主你好，</p><p>请问你的4218324716.txt是以什么规律命名的？</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=439#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-439', 439);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-440" class="comment-body comment-child comment-level-odd comment-odd comment-by-author">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/5eceb4876d630f1289e2b34a645903fd?s=32&amp;r=X&amp;d=" alt="Cannikin" width="32" height="32" />        <cite class="fn"><a href="https://www.e-fly.org" rel="external nofollow">Cannikin</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-440">December 8th, 2014 at 04:11 pm</a>
            </div>
    <div class="comment-content">
    <p>随机，无规律。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=440#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-440', 440);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-441" class="comment-body comment-child comment-level-even comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/13fe3c1d0a0e692bc81226c99418834d?s=32&amp;r=X&amp;d=" alt="rurgieo" width="32" height="32" />        <cite class="fn">rurgieo</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-441">December 8th, 2014 at 04:41 pm</a>
            </div>
    <div class="comment-content">
    <p>好吧，那我只能抓取HTML里面的链接了~~<br>
另外能否给我个TVlist的播放源啊，我看你给过别人源码的，谢谢啦</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=441#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-441', 441);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-442" class="comment-body comment-child comment-level-odd comment-odd comment-by-author">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/5eceb4876d630f1289e2b34a645903fd?s=32&amp;r=X&amp;d=" alt="Cannikin" width="32" height="32" />        <cite class="fn"><a href="https://www.e-fly.org" rel="external nofollow">Cannikin</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-442">December 8th, 2014 at 09:32 pm</a>
            </div>
    <div class="comment-content">
    <p>直接另存为页面就可以了，本身就是第三方播控平台。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=442#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-442', 442);">回复</a>    </div>
    </li>
</ol>    </div>
    </li>
</ol>    </div>
    </li>
</ol>    </div>
    </li>
<li id="comment-436" class="comment-body comment-parent comment-even">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/727441e76c911bcd2bd2c60babff8b77?s=32&amp;r=X&amp;d=" alt="jjjjjjjjjjjjjjjjjjjjjjjjjjjjj" width="32" height="32" />        <cite class="fn">jjjjjjjjjjjjjjjjjjjjjjjjjjjjj</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-436">December 6th, 2014 at 11:23 pm</a>
            </div>
    <div class="comment-content">
    <p>楼主既然提供IP 为何DNS要用国内的？</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=436#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-436', 436);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-438" class="comment-body comment-child comment-level-odd comment-odd comment-by-author">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/5eceb4876d630f1289e2b34a645903fd?s=32&amp;r=X&amp;d=" alt="Cannikin" width="32" height="32" />        <cite class="fn"><a href="https://www.e-fly.org" rel="external nofollow">Cannikin</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-438">December 7th, 2014 at 10:15 am</a>
            </div>
    <div class="comment-content">
    <p>纠结于截图真的好吗？</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=438#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-438', 438);">回复</a>    </div>
    </li>
</ol>    </div>
    </li>
<li id="comment-432" class="comment-body comment-parent comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/8932c14edb574727ad7b5b305334786b?s=32&amp;r=X&amp;d=" alt="fupeng" width="32" height="32" />        <cite class="fn">fupeng</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-432">December 5th, 2014 at 10:41 pm</a>
            </div>
    <div class="comment-content">
    <p>首先感谢楼主不间断的向广大网友提供未被污染的IP，非常感谢！<br>
在此，提出一个小小的建议：由于几乎每天都要手动的更新IP，感觉非常麻烦，所以想做一个自动更新IP的程序，楼主能提供获取新IP的接口，然后运行GoAgent时，自动先跟新到最新的IP，就不用手动做了。希望楼主采纳！谢谢! Email：fuxp90@gmail.com</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=432#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-432', 432);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-433" class="comment-body comment-child comment-level-odd comment-odd comment-by-author">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/5eceb4876d630f1289e2b34a645903fd?s=32&amp;r=X&amp;d=" alt="Cannikin" width="32" height="32" />        <cite class="fn"><a href="https://www.e-fly.org" rel="external nofollow">Cannikin</a></cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-433">December 5th, 2014 at 10:48 pm</a>
            </div>
    <div class="comment-content">
    <p>感谢你的热心建议，目前网站无此类接口功能，你也可以看到，每次的更新都是一个txt的文本文件而已。如果博客程序有类似更新，我必会通知你。<br>
在此说明一下，所提供的IP只为更好的满足查阅学习之用，希望各位朋友尽量减少浏览不合乎大陆政策的内容，确保IP的使用长久性，满足更多有需求的朋友。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=433#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-433', 433);">回复</a>    </div>
        <div class="comment-children">
        <ol class="comment-list"><li id="comment-435" class="comment-body comment-child comment-level-even comment-odd">
    <div class="comment-author">
        <img class="avatar" src="https://secure.gravatar.com/avatar/00dafc6798af91c535623598c2d2176a?s=32&amp;r=X&amp;d=" alt="Nom" width="32" height="32" />        <cite class="fn">Nom</cite>
    </div>
    <div class="comment-meta">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1#comment-435">December 6th, 2014 at 09:20 am</a>
            </div>
    <div class="comment-content">
    <p>LZ的愿望是好的，但是现实是残酷的。即使上上twitter和G+都被有关部门认为是不和谐，所以，哎，不说了。</p>    </div>
    <div class="comment-reply">
        <a href="https://cb.e-fly.org/archives/goagent-iplist.html/comment-page-1?replyTo=435#respond-post-270" rel="nofollow" onclick="return TypechoComment.reply('comment-435', 435);">回复</a>    </div>
    </li>
</ol>    </div>
    </li>
</ol>    </div>
    </li>
</ol>            

            

                        <div id="respond-post-270" class="respond">

            

            <div class="cancel-comment-reply">

            <a id="cancel-comment-reply-link" href="https://cb.e-fly.org/archives/goagent-iplist.html#respond-post-270" rel="nofollow" style="display:none" onclick="return TypechoComment.cancelReply();">取消回复</a>            </div>

            

			<h4 id="response">Post a new comment &raquo;</h4>

			<form method="post" action="https://cb.e-fly.org/archives/goagent-iplist.html/comment" id="comment_form">

                				<p>

                    <label for="author">Name<span class="required">*</span></label>

					<input type="text" name="author" id="author" class="text" size="15" value="" />

				</p>

				<p>

                    <label for="mail">Email<span class="required">*</span></label>

					<input type="text" name="mail" id="mail" class="text" size="15" value="" />

				</p>

				<p>

                    <label for="url">Website (optional)</label>

					<input type="text" name="url" id="url" class="text" size="15" value="" />

				</p>

                				<p><textarea rows="5" cols="50" name="text" class="textarea"></textarea></p><p><img src="https://cb.e-fly.org/action/captcha" alt="captcha" onclick="this.src = this.src + '?' + Math.random()" style="cursor: pointer" title="点击图片刷新验证码" /><br /><input type="text" class="captcha" name="captcha_code" /> <strong>请输入验证码</strong></p>

				<p><input type="submit" value="Submit Comment" class="submit" /></p>

			</form>

            </div>

            		</div>    </div><!-- end #content-->

	    <div class="grid_4" id="sidebar">



            

        

                <div class="widget">

			<h3>Category</h3>

            <ul>

                <li><a href="https://cb.e-fly.org/category/Operating-System/">System</a> (40)</li>
<li><a href="https://cb.e-fly.org/category/Security/">Security</a> (5)</li>
<li><a href="https://cb.e-fly.org/category/Hardware/">Hardware</a> (10)</li>
<li><a href="https://cb.e-fly.org/category/Collection/">Collection</a> (3)</li>
<li><a href="https://cb.e-fly.org/category/application/">Application</a> (17)</li>
<li><a href="https://cb.e-fly.org/category/cb/">Cubieboard</a> (42)</li>
<li><a href="https://cb.e-fly.org/category/Pi/">Raspberry Pi</a> (26)</li>
<li><a href="https://cb.e-fly.org/category/Other/">Other</a> (3)</li>
            </ul>

		</div>

        

        

        		<div class="widget">

			<h3>Other</h3>

            <ul>

                                    <li class="last"><a href="https://cb.e-fly.org/admin/login.php">Login</a></li>

                                <li><a href="https://cb.e-fly.org/aggregation.html">资源聚合</a></li>

                <li><a href="https://cb.e-fly.org/coreprotect/" target="_blank">Core Protect</a></li>

                <li><a href="http://validator.w3.org/check/referer" target="_blank">Valid XHTML</a></li>

            </ul>

		</div>

		<div class="widget">

			<h3>Link</h3>

            <ul>

                <li><a href="http://v.2345.com/?k253039" target="_blank">影视大全</a></li>

                <li><a href="http://www.cubieboard.org" target="_blank">Cubieboard.org</a></li>

                <li><a href="http://docs.cubieboard.org" title="Cubieboard Docs" target="_blank">Cubieboard Docs</a></li>

                <li><a href="http://dl.cubieboard.org" title="System Download" target="_blank">Cubie Download</a></li>

                <li><a href="http://forum.cubietech.com" title="中文官方论坛" target="_blank">Cubie 中文官方论坛</a></li>

            </ul>

		</div>

		<div class="widget">

			<h3>Blogroll</h3>

            <ul>

                <script type="text/javascript" src="https://tajs.qq.com/stats?sId=24942598" charset="UTF-8"></script>

                <li><a href="http://just4fun.cn/" title="乐趣为王" target="_blank">乐趣为王</a></li>

                <li><a href="http://svr.weirm.info:81" title="万致远博客" target="_blank">万致远博客</a></li>

                <li><a href="http://www.lianst.com/" title="连仕彤博客" target="_blank">连仕彤博客</a></li>

                <li><a href="http://march.zmyseries.com/blog/" title="march's blog" target="_blank">march's blog</a></li>

                <li><a href="http://rance.rdy2.com:81/" title="Rance has home with Amanda" target="_blank">Rance&Amanda home</a></li>

            </ul>

		</div>

		<div class="widget">

			<h3>期待您的支持</h3>

            <ul>

                轻点一次文章广告即是对我的回应

            </ul>

		</div>

        

    </div><!-- end #sidebar -->		<div class="grid_14" id="footer">

	&copy; Powered by Typecho &amp; (&alpha;)Cannikin<br /><a href="https://cb.e-fly.org/feed/" target="_blank">Article RSS</a> and <a href="https://cb.e-fly.org/feed/comments/" target="_blank">Comment RSS</a><br /><img alt="Web" src="/usr/themes/default/images/web.png" />

	</div><!-- end #footer -->

</div>

<script src="https://cb.e-fly.org/usr/plugins/Announcement/js/jquery.min.js"></script><link href="https://cb.e-fly.org/usr/plugins/Announcement/css/style.css" type="text/css" rel="stylesheet" /><script src="https://cb.e-fly.org/usr/plugins/Announcement/js/script.js" type="text/javascript"></script><span id="announcement_plug" data-type="2" data-content="2014.11.14 , 网站启用SSL加密访问,请朋友们使用 HTTPS://CB.E-FLY.ORG 进行访问.

2014.10.24 , 如有个别地区IP失效迅速,还请及时留言告知,方便博主及时更新.

2014.10.22 , 因为数据库操作失败,站点数据回溯多天."></span></body>

</html>"""