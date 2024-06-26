import dtlpy as dl

package_name = 'logs-function'
project_name = 'My Project'
src_path = 'functions/view_service_logs'

project = dl.projects.get(project_name=project_name)

####################
# Push the Package #
####################
modules = dl.PackageModule(name='default',
                           entry_point='main.py',
                           functions=[dl.PackageFunction(name='run',
                                                         inputs=dl.FunctionIO(type='Item', name='item'))])
package = project.packages.push(package_name=package_name,
                                modules=modules,
                                src_path=src_path)
package = project.packages.get(package_name=package_name)
package.print()

##################
# Create service #
##################
service = package.services.deploy(service_name=package.name,
                                  package=package,
                                  runtime={'gpu': False,
                                           'numReplicas': 1,
                                           'concurrency': 32,
                                           },
                                  module_name='default'
                                  )
print('Service deployed successfully!')
# # Updating existing service
# service = package.services.get(service_name=package.name)
# service.package_revision = package.version
# service.update()

######################
# Execute a Function #
######################
service = package.services.get(service_name='dummy-function')
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
execution = service.execute(execution_input=[dl.FunctionIO(type='Item',
                                                           value={'item_id': item.id},
                                                           name='item')],
                            function_name='run')

# stream logs with follow
execution.logs(follow=True)
