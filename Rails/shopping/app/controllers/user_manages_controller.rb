class UserManagesController < ApplicationController
  before_action :authenticate_user!

  def index
    if current_user.is_admin?
      @users = User.all
    else
      redirect_to user_manage_path(current_user)
    end
  end

  def show
    if current_user.is_admin?
      @user = User.find_by(id: params[:id])
    else
      @user = current_user
    end
  end

  def update
    current_user.update(user_param)
    redirect_to user_manage_path(current_user)
  end

  private
  def user_param
    if params.require(:user).permit(:password)['password'] == '' and params.require(:user).permit(:current_password,)['current_password,'] == '' and params.require(:user).permit(:password_confirmation)['password_confirmation'] == ''
      params.require(:user).permit(:email, :name, :nickname, :phone, :phone_memo)
    else
      params.require(:user).permit(:password, :password_confirmation)
    end
  end
end
