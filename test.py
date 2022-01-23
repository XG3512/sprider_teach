html_doc = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello World</h4>   
    </div>

    <div class="panel-body">
        <ul class="list" id="list-1">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>

        <ul class="list list-samll" id="list-2">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
    </div>
    </div>
</div>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.select('.panel .panel-heading'))  # 获取class为panel-heading的节点
print(soup.select('ul li'))  # 获取ul下的li节点
print(soup.select('#list-2 li'))  # 获取id为list-2下的li节点
print(soup.select('ul'))  # 获取所有的ul节点
print(type(soup.select('ul')[0]))

for li in soup.select('li'):
    print('String:', li.string)
    print('get text:', li.get_text())