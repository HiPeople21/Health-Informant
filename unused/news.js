var country = {{content['country']|safe}};
var template = document.querySelector('#news-template');
var sentinel = document.querySelector('#sentinel');
var newsContainer = document.querySelector('.news-container');
var page = 0;

function loadNews() {
			$.ajax({
			data : {
				country: country,
        page: page,
			},
			type : 'POST',
			url : '/load-news'
		})
		.done(function(data) {
      for (news of data) {
        let templateClone = template.content.cloneNode(true);

        templateClone.querySelector(".news-publisher").innerHTML = `${news['publisher']}`;
        templateClone.querySelector(".news-title").innerHTML = `${news['title']}`;
        templateClone.querySelector(".news-text").innerHTML = `${news['text']}`;
        templateClone.querySelector(".news-item-link").href = `${news['link']}`;
        templateClone.querySelector(".news-time").innerHTML = `${news['time']}`;

        newsContainer.appendChild(templateClone);
        page += 10;
      }
		});
}

var intersectionObserver = new IntersectionObserver(entries => {

  
  if (entries[0].intersectionRatio <= 0) {
    return;
  }

  loadNews();

});

intersectionObserver.observe(sentinel);