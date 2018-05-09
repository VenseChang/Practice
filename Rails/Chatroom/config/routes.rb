Rails.application.routes.draw do
  get 'chats/index'

  get 'chats/show'

  root "chats#index"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  mount ActionCable.server => '/cable'
end
