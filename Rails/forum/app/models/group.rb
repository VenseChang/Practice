class Group < ApplicationRecord
  validates :title, presence: true

  has_many :posts
  belongs_to :owner, class_name: "User", foreign_key: :user_id

  has_many :group_users
  has_many :members, through: :group_users, source: :user

  def editable_by?(user)
    user && user == owner
  end
end
