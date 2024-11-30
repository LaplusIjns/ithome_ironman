<!DOCTYPE html><html><head><meta charset="utf-8"><title>BingTranslation.md</title><style></style></head><body id="preview">
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="ithome_ironman_0"></a>ithome_ironman</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">用於爬取 IT邦幫忙的爬蟲工具,可以根據關鍵字過濾出相關文章。</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Features_4"></a>Features</h2>
<ul>
<li class="has-line-data" data-line-start="5" data-line-end="6">支持多線程爬取</li>
<li class="has-line-data" data-line-start="6" data-line-end="7">可設定關鍵字過濾</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">輸出JSON格式結果</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">分類相關主題</li>
</ul>
<h2 class="code-line" data-line-start=9 data-line-end=10 ><a id="_9"></a>使用</h2>
<p class="has-line-data" data-line-start="11" data-line-end="12">請先確認本機已安裝python</p>
<pre><code class="has-line-data" data-line-start="14" data-line-end="16" class="language-python">  pip install -r requirements.txt
</code></pre>
<p class="has-line-data" data-line-start="17" data-line-end="20">在 <a href="http://script.py">script.py</a> 中設定<br>
include_keyword = [‘java’,‘spring’] # 要包含的關鍵字<br>
exclude_keyword = [‘javascript’] # 要排除的關鍵字</p>
<pre><code class="has-line-data" data-line-start="21" data-line-end="23">python script.py
</code></pre>
<p class="has-line-data" data-line-start="23" data-line-end="24">搜尋後產生 result.json</p>
<pre><code class="has-line-data" data-line-start="25" data-line-end="30" class="language-json">{
    "<span class="hljs-attribute">title</span>": <span class="hljs-value"><span class="hljs-string">"標題"</span></span>,
    "<span class="hljs-attribute">href</span>": <span class="hljs-value"><span class="hljs-string">"連結"</span>
</span>}
</code></pre>
<p class="has-line-data" data-line-start="31" data-line-end="32">之後執行</p>
<pre><code class="has-line-data" data-line-start="33" data-line-end="35">python script_parse.py
</code></pre>
<p class="has-line-data" data-line-start="36" data-line-end="38">將產出文章主要主題與相關連結<br>
存於 result_main_subject.json</p>
<pre><code class="has-line-data" data-line-start="39" data-line-end="50" class="language-json">{
    "<span class="hljs-attribute">title</span>": <span class="hljs-value"><span class="hljs-string">"主題"</span></span>,
    "<span class="hljs-attribute">href</span>": <span class="hljs-value"><span class="hljs-string">"主題連結"</span></span>,
    "<span class="hljs-attribute">child</span>": <span class="hljs-value">[
        {
                "<span class="hljs-attribute">title</span>": <span class="hljs-value"><span class="hljs-string">"文章標題"</span></span>,
                "<span class="hljs-attribute">href</span>": <span class="hljs-value"><span class="hljs-string">"文章連結"</span>
        </span>}
    ]
</span>}
</code></pre>

</body></html>