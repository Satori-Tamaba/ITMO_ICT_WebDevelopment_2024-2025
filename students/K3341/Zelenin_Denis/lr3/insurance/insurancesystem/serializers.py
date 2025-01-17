from rest_framework import serializers

from .models import *


class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'


class InsuranceAgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceAgents
        fields = '__all__'


class InsuranceCotractsSerializer(serializers.ModelSerializer):
    AgentID = serializers.PrimaryKeyRelatedField(queryset=InsuranceAgents.objects.all())
    OrganizationID = serializers.PrimaryKeyRelatedField(queryset=Organizations.objects.all())

    class Meta:
        model = InsuranceCotracts
        fields = '__all__'


class InsuranceCasesSerializer(serializers.ModelSerializer):
    CotractID = InsuranceCotractsSerializer(read_only=True)

    class Meta:
        model = InsuranceCases
        fields = '__all__'


class AgentContractsSerializer(serializers.ModelSerializer):
    AgentID = InsuranceAgentsSerializer(read_only=True)

    class Meta:
        model = AgentContracts
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    OrganizationID = serializers.PrimaryKeyRelatedField(queryset=Organizations.objects.all())

    class Meta:
        model = Employees
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['OrganizationID'] = OrganizationsSerializer(instance.OrganizationID).data
        return rep


class CategoryPaymentsSerializer(serializers.ModelSerializer):
    ContractID = InsuranceCotractsSerializer(read_only=True)

    class Meta:
        model = CategoryPayments
        fields = '__all__'
