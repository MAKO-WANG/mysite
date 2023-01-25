from rest_framework import serializers
from .models import StudentList, SubjectList, Fraction


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=64)
    sex = serializers.ChoiceField(
        choices=StudentList.sex_choices, required=False)
    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return StudentList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.save()
        return instance


class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=64)
    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return SubjectList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class FractionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student = serializers.CharField(
        required=False, allow_blank=True)
    subject = serializers.CharField(max_length=64)
    fraction = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Fraction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student = validated_data.get('student', instance.student)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.save()
        return instance

    def validate(self, attrs):
        student = attrs.get('student', '')
        subject = attrs.get('subject', '')
        if student:
            student = StudentList.objects.filter(name=student).first()
            if student is not None:
                attrs['student'] = student
            else:
                raise serializers.ValidationError(detail='没有学生信息')
        if subject:
            subject = SubjectList.objects.filter(name=subject).first()
            if subject is not None:
                attrs['subject'] = subject
            else:
                raise serializers.ValidationError(detail='没有学科信息')
        return super().validate(attrs)
