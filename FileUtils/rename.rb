#coding:utf-8


def list_current_dir
	Dir.glob('**/*').each {|file| puts file}
end
def list_dir(file_path)
	Dir.foreach(file_path) { |file| puts file }
end
def traverse_dir(file_path)
    if File.directory? file_path
        Dir.foreach(file_path) do |file|
            if file !="." and file !=".."
                traverse_dir(file_path+"/"+file)
            end
        end
    else
        puts "File:#{File.basename(file_path)}, Size:#{File.size(file_path)}"
    end
end

filePath='/Users/cym/project/ruby/rails3'
list_current_dir
#traverse_dir('/Users/cym/project/ruby/rails3')

