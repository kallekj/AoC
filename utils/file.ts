type Separator = string | RegExp;

export function splitFile(content: string, splitters: Separator[]){
    return splitters.map(splitter => {
        const data = content.split(splitter);
        console.log(data);
        return data;
    });
}