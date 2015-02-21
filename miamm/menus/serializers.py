from rest_framework import serializers
from recipes.serializers import RecipeSerializer
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from menus.models import Day, Menu, Week, MenuUser


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('dinner','supper',)


class WeekSerializer(serializers.ModelSerializer):
    sunday = DaySerializer()
    monday = DaySerializer()
    tuesday = DaySerializer()
    wednesday = DaySerializer()
    thursday = DaySerializer()
    friday = DaySerializer()
    saturday = DaySerializer()
    class Meta:
        model = Week
        fields = ('number','sunday','monday','tuesday','wednesday','thursday','friday','saturday',)

    def create(self, validated_data):
        menu = validated_data.get('menu')
        week_number = validated_data.get('number')
        existing_week = Week.objects.filter(menu=menu, number=week_number)
        if len(existing_week) > 0:
            raise serializers.ValidationError('This is already a week number '+str(week_number))

        sunday_data = validated_data.pop('sunday')
        sunday = Day.objects.create(**sunday_data)
        monday_data = validated_data.pop('monday')
        monday = Day.objects.create(**monday_data)
        tuesday_data = validated_data.pop('tuesday')
        tuesday = Day.objects.create(**tuesday_data)
        wednesday_data = validated_data.pop('wednesday')
        wednesday = Day.objects.create(**wednesday_data)
        thursday_data = validated_data.pop('thursday')
        thursday = Day.objects.create(**thursday_data)
        friday_data = validated_data.pop('friday')
        friday = Day.objects.create(**friday_data)
        saturday_data = validated_data.pop('saturday')
        saturday = Day.objects.create(**saturday_data)
        week = Week.objects.create(sunday=sunday,
                                   monday=monday,
                                   tuesday=tuesday,
                                   wednesday=wednesday,
                                   thursday=thursday,
                                   friday=friday,
                                   saturday=saturday,
                                   **validated_data)

        return week

    def update(self,instance, validated_data):
        week_number = validated_data.get('number')
        if week_number != instance.number:
            menu = instance.menu
            existing_week = Week.objects.filter(menu=menu, number=week_number)
            if len(existing_week) > 0:
                raise serializers.ValidationError('This is already a week number '+str(week_number))
        sunday_data = validated_data.pop('sunday')
        instance.sunday.dinner = sunday_data.get('dinner')
        instance.sunday.supper = sunday_data.get('supper')
        monday_data = validated_data.pop('monday')
        instance.monday.dinner = monday_data.get('dinner')
        instance.monday.supper = monday_data.get('supper')
        tuesday_data = validated_data.pop('tuesday')
        instance.tuesday.dinner = tuesday_data.get('dinner')
        instance.tuesday.supper = tuesday_data.get('supper')
        wednesday_data = validated_data.pop('wednesday')
        instance.wednesday.dinner = wednesday_data.get('dinner')
        instance.wednesday.supper = wednesday_data.get('supper')
        thursday_data = validated_data.pop('thursday')
        instance.thursday.dinner = thursday_data.get('dinner')
        instance.thursday.supper = thursday_data.get('supper')
        friday_data = validated_data.pop('friday')
        instance.friday.dinner = friday_data.get('dinner')
        instance.friday.supper = friday_data.get('supper')
        saturday_data = validated_data.pop('saturday')
        instance.saturday.dinner = saturday_data.get('dinner')
        instance.saturday.supper = saturday_data.get('supper')

        instance.number = validated_data.pop('number')

        instance.save()

        return instance


class MenuUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuUser
        fields = ('id', 'user')

    def create(self, validated_data):
        menu = validated_data.get('menu')
        user = validated_data.pop('user')
        existing_user = MenuUser.objects.filter(menu=menu, user=user)
        if len(existing_user) > 0:
            raise serializers.ValidationError('This user: '+ user.username +' is already in the menu')
        menuuser = MenuUser.objects.create(user=user, **validated_data)

        return menuuser

    def update(self, instance, validated_data):
        user = validated_data.pop('user')

        if instance.user != user:
            menu = instance.menu
            existing_user = MenuUser.objects.filter(menu=menu, user=user)
            if len(existing_user) > 0:
                raise serializers.ValidationError('This user: '+ user.username +' is already in the menu')
            instance.user = user

        instance.save()

        return instance


class MenuSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True,read_only=True)
    users = MenuUserSerializer(many=True,read_only=True)

    class Meta:
        model = Menu
        fields = ('name','owner', 'users','weeks')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
