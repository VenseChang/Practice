class ProductsController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show]
  before_action :find_product, only: [:edit, :update, :destroy, :shopping_cart]
  before_action :product_kind, only: [:new, :create, :edit, :update]

  def index
    @products = Product.where("amount > 0")
    @kinds = Kind.all
  end

  def new
    @product = Product.new
  end

  def create
    @product = Product.new(product_params)
    if @product.save
      redirect_to product_manages_path
    else
      render :new
    end
  end

  def edit
  end

  def update
    if @product.update(product_params)
      redirect_to product_manages_path
    else
      render :edit
    end
  end

  def show
    @product = Product.includes(:product_pictures).find_by(id: params[:id])
    @shopping_cart = (current_user and current_user.shopping_carts.exists?(product_id: params[:id]))? current_user.shopping_carts.find_by(product_id: params[:id]) : ShoppingCart.new(amount: 1)
  end

  def shopping_cart
    exist = current_user.shopping_carts.exists?(product_id: params[:id])
    cart_amount = (exist)? current_user.shopping_carts.find_by(product_id: params[:id]).amount : 0
    amount = (params.key? :shopping_cart)? params.require(:shopping_cart).permit(:amount)["amount"].to_i : 1
    if amount  > @product.amount
      flash[:alert] = "數量不可大於庫存"
    else
      shopping_cart_save amount, cart_amount, exist
    end
    redirect_back fallback_location: root_path
  end

  def search
    @products = Product.where("name LIKE ?", "%#{params.require(:product).permit(:name)['name']}%")
    render template:  "products/index"
  end

  private
  def shopping_cart_save amount, cart_amount, product_exist
    if @product.update(amount: @product.amount - amount)
      if !product_exist
        shopping_cart = current_user.shopping_carts.new(product_id: @product.id, amount: amount)
        shopping_cart.save
      else
        current_user.shopping_carts.find_by(product_id: params[:id]).update(amount: (cart_amount + amount))
      end
    end
  end

  def product_kind
    @kinds = Kind.all
  end

  def find_product
    @product = Product.find_by(id: params[:id])
  end

  def product_params
    params.require(:product).permit(:name, :price, :amount, :description, :content, :kind_id, :image)
  end
end
