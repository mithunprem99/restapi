from rest_framework import serializers
from .models import Customer,Products
from rest_framework.serializers import ModelSerializer
from datetime import datetime,timezone
from django.utils.timesince import timesince
from datetime import date
from datetime import timedelta


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model= Customer
		fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
	# see=CustomerSerializer(many=True, read_only=True)
	# p_status = serializers.BooleanField(required=True)
	# value_id = serializers.IntegerField(required=False)
	time_since_add=serializers.SerializerMethodField()
	class Meta:
		model = Products 
		fields = '__all__'

	def get_time_since_add(self,object):
		now=datetime.now(timezone.utc)
		published_date=object.p_add_date
		# time_delta = timesince(published_date,now)
		time_delta = now.date() - datetime.date(published_date)
		return time_delta.days

		# if object.p_status == True:
		# 	if time_delta.days<60:
		# 			raise serializers.ValidationError("can inactive only after 60 days")
		# return time_delta.days
		# return [time_delta.days,object.p_status]

	# p_status = serializers.BooleanField(required=True)

	def validate_p_add_date(self,datevalue):
		# today=date.today()
		# status=p_status
		# if status==false:
			if ("datevalue<60"):
				raise serializers.ValidationError("can inactive only after 60 days")
			return object

