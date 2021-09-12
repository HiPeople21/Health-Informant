$(function() {
  $('.news-form-container').on('submit', function() {
    $('.form-submit-button').html('<span class="loading-spinner spinner-border spinner-border-sm" role="status"></span> Loading...');
  });
  $('.covid-form').on('submit', function() {
    $('.form-submit-button').html('<span class="loading-spinner spinner-border spinner-border-sm" role="status"></span> Loading...');
  });
});
