CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.indentClasses = ["ul-grey", "ul-red", "text-red", "ul-content-red", "circle", "style-none", "decimal", "paragraph-portfolio-top", "ul-portfolio-top", "url-portfolio-top", "text-grey"];
	//config.contentsCss = ["/css/bootstrap.css", "/css/styles.css"];
	config.contentsCss = ["/css/styles.css"];
	customConfig: '/js/bootstrap.min.js';
	config.bodyClass = 'mystyle';
	config.protectedSource.push(/<(style)[^>]*>.*<\/style>/ig);
	config.protectedSource.push(/<(script)[^>]*>.*<\/script>/ig);// разрешить теги <script>
	config.protectedSource.push(/<(i)[^>]*>.*<\/i>/ig);// разрешить теги <i>
	config.protectedSource.push(/<\?[\s\S]*?\?>/g);// разрешить php-код
	config.protectedSource.push(/<!--dev-->[\s\S]*<!--\/dev-->/g);
	config.allowedContent = true;
	config.disableNativeSpellChecker = false;
	config.extraPlugins = 'btgrid,youtube,bootstrapTabs,bgimage,lineheight,html5video,codesnippet,collapsibleItem,tableresize,ckawesome';
	config.fontawesomePath = '/js/ckeditor/plugins/fontawesome/font-awesome/css/font-awesome.min.css';
	config.codeSnippet_languages = {
    javascript: 'JavaScript',
    php: 'PHP',
		html: 'HTML',
		css: 'CSS',
		mysql: 'MYSQL'
	};	
	config.removePlugins = 'contextmenu, spellchecker, about, save, newpage, print, templates, scayt, flash, pagebreak, smiley,preview,find'
};